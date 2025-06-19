# 🧠 Model Context Protocol (MCP) — Structured Notes

## ❌ What MCP is Not
- Not a framework for building agents
- Not a way to code agents
- Not a fundamental change to how agents work

## ✅ What MCP Is
- A protocol — a standard
- A simple way to integrate tools, resources, and prompts
- Think of it as the USB-C port for AI applications

## 🔑 MCP Core Concepts
MCP is built on three main components:

### Host
- An LLM application (e.g., Claude, or a custom agent architecture)

### MCP Client
- Resides within the Host
- Connects 1:1 to an MCP Server

### MCP Server
- Provides tools, context, and prompts to the Host via the Client

## 📘 Example
`fetch` is an MCP server that searches the web using a headless browser.

You can configure a Claude desktop app (the Host) to:
- Run an MCP client
- That launches the `fetch` MCP server locally on your machine

## 🏗️ MCP Architecture
Here's a simplified architecture diagram:

![MCP ARCHITECTURE](mcp.png)

