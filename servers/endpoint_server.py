from fastmcp import FastMCP
import requests

mcp = FastMCP("endpoint-server")

@mcp.tool()
def fetch_url(url: str) -> str:
    """Fetch content from a web URL."""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.text
    except Exception as e:
        return f"Error fetching {url}: {e}"

if __name__ == "__main__":
    mcp.run()
