#!/usr/bin/ENV python3
"""Programming Learning MCP Server"""

from fastmcp import FastMCP

mcp = FastMCP("Programming Learning Server")

if __name__ == "__main__":
    mcp.run()