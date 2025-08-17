# Normal MCP Server (HTTP+SSE Transport)

The original MCP implementation used HTTP + Server-Sent Events (SSE), which had these characteristics:

- **Two separate endpoints**: Required maintaining two separate endpoints - one for SSE connections and another for POST requests (`/messages`) [Understanding MCP Recent Change Around HTTP+SSE – ceposta Technology Blog](https://blog.ceposta.com)
- **Two separate connections**: One for server→client communication (SSE) and one for client→server communication (HTTP POST)
- **Complex setup**: Client connects to an SSE endpoint, server responds with an "endpoint event" telling the client what URI to use for sending messages

# Streamable MCP Server (Streamable HTTP Transport)

MCP introduces Streamable HTTP for remote servers in recent updates. In simple terms, this means we don't need to have two separate endpoints. The client can stream responses from the server directly from the `/messages` endpoint. [Understanding MCP Recent Change Around HTTP+SSE – ceposta Technology Blog](https://blog.ceposta.com)

Key advantages of streamable MCP servers:

- **Single endpoint**: The server can decide whether it will respond with a streamable response or standard HTTP response [Understanding MCP Recent Change Around HTTP+SSE – ceposta Technology Blog](https://blog.ceposta.com)
- **Simplified architecture**: Plain HTTP implementation - MCP can now be implemented in a plain HTTP server without requiring separate SSE support, simplifying server implementation
- **Better infrastructure compatibility**: Being "just HTTP" ensures compatibility with standard middleware and infrastructure
- **Flexible implementation**: Supports both stateless and stateful server implementations
- **Dynamic streaming**: The server can dynamically decide whether to respond with a standard HTTP response or upgrade to streaming based on the specific interaction needs

# Why the Change?

The HTTP+SSE approach had limitations including:
- Requiring maintaining two separate connections/endpoints
- Necessitating persistent connections making stateless implementations difficult
- Having limited compatibility with some infrastructure and middleware

The streamable HTTP transport represents a significant improvement because:
- It simplifies the protocol by using a single connection point
- Allows servers to be more flexible about when to use streaming vs. one-time responses
- Enables completely stateless server implementations when appropriate

In essence, streamable MCP servers offer a more modern, flexible, and infrastructure-friendly approach to implementing the Model Context Protocol while maintaining all the functionality of the original specification.