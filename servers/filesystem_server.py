from fastmcp import FastMCP
import os

mcp = FastMCP("filesystem-server")

@mcp.tool()
def read_file(path: str) -> str:
    """Read text content from a file."""
    if not os.path.exists(path):
        return f"File not found: {path}"
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

if __name__ == "__main__":
    mcp.run()
