#!/usr/bin/env node
// Smoke-test client for the Open-Meteo MCP server configured in .mcp.json.
// Launches the server exactly as Claude Code would, performs the MCP handshake
// over stdio and calls one tool. Used to verify the integration and to record
// real MCP responses for run artifacts. No API key, no secrets.
//
// Usage:
//   node scripts/mcp_weather_probe.mjs --list
//   node scripts/mcp_weather_probe.mjs <tool-name> '<json-arguments>'
// Example:
//   node scripts/mcp_weather_probe.mjs geocoding '{"name":"Warsaw"}'

import { spawn } from "node:child_process";
import { readFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const repoRoot = join(dirname(fileURLToPath(import.meta.url)), "..");
const config = JSON.parse(readFileSync(join(repoRoot, ".mcp.json"), "utf-8"));
const server = config.mcpServers["open-meteo"];

const [mode, toolArg] = process.argv.slice(2);
if (!mode) {
  console.error("usage: mcp_weather_probe.mjs --list | <tool> '<json-args>'");
  process.exit(2);
}

const child = spawn(
  [server.command, ...server.args.map((arg) => JSON.stringify(arg))].join(" "),
  {
    cwd: repoRoot,
    env: { ...process.env, ...(server.env ?? {}) },
    shell: true,
    windowsHide: true,
    stdio: ["pipe", "pipe", "pipe"],
  },
);

let buffer = "";
const pending = new Map();
let nextId = 1;

child.stdout.on("data", (chunk) => {
  buffer += chunk.toString();
  let idx;
  while ((idx = buffer.indexOf("\n")) >= 0) {
    const line = buffer.slice(0, idx).trim();
    buffer = buffer.slice(idx + 1);
    if (!line) continue;
    let message;
    try {
      message = JSON.parse(line);
    } catch {
      continue;
    }
    if (message.id !== undefined && pending.has(message.id)) {
      pending.get(message.id)(message);
      pending.delete(message.id);
    }
  }
});

child.stderr.on("data", (chunk) => process.stderr.write(chunk.toString()));

function request(method, params) {
  const id = nextId++;
  const payload = { jsonrpc: "2.0", id, method, params };
  return new Promise((resolve, reject) => {
    const timer = setTimeout(() => {
      pending.delete(id);
      reject(new Error(`timeout waiting for ${method}`));
    }, 90000);
    pending.set(id, (message) => {
      clearTimeout(timer);
      if (message.error) reject(new Error(`${method}: ${JSON.stringify(message.error)}`));
      else resolve(message.result);
    });
    child.stdin.write(JSON.stringify(payload) + "\n");
  });
}

function notify(method, params) {
  child.stdin.write(JSON.stringify({ jsonrpc: "2.0", method, params }) + "\n");
}

try {
  const init = await request("initialize", {
    protocolVersion: "2024-11-05",
    capabilities: {},
    clientInfo: { name: "mcp-weather-probe", version: "1.0.0" },
  });
  notify("notifications/initialized", {});
  console.error(`connected: ${init.serverInfo?.name ?? "unknown server"}`
    + ` ${init.serverInfo?.version ?? ""}`.trimEnd());

  if (mode === "--list") {
    const result = await request("tools/list", {});
    for (const tool of result.tools ?? []) console.log(`${tool.name}\t${tool.description ?? ""}`);
  } else if (mode === "--schema") {
    const result = await request("tools/list", {});
    const tool = (result.tools ?? []).find((entry) => entry.name === toolArg);
    if (!tool) throw new Error(`unknown tool: ${toolArg}`);
    console.log(JSON.stringify(tool.inputSchema, null, 2));
  } else {
    let args = {};
    if (toolArg?.startsWith("@")) {
      args = JSON.parse(readFileSync(toolArg.slice(1), "utf-8"));
    } else if (toolArg) {
      args = JSON.parse(toolArg);
    }
    const result = await request("tools/call", { name: mode, arguments: args });
    for (const item of result.content ?? []) {
      if (item.type === "text") console.log(item.text);
    }
    if (result.isError) process.exitCode = 1;
  }
} catch (error) {
  console.error(`mcp_weather_probe: ${error.message}`);
  process.exitCode = 1;
} finally {
  child.kill();
}
