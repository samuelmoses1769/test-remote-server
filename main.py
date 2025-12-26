from fastmcp import FastMCP
import random
import json

mcp=FastMCP('Simple Model')


@mcp.tool
def add_numbers(a: int, b: int) -> int:
    """Add two numbers and return the result."""
    return a + b

@mcp.tool
def get_random_number(min_value: int, max_value: int) -> int:
    """Generate a random number between min_value and max_value."""
    return random.randint(min_value, max_value)

@mcp.resource("info://server")
def server_info() -> str:
    """Return server information in JSON format."""
    info = {
        "server_name": "FastMCP Server",
        "version": "1.0.0",
        "uptime": "48 hours",
        "active_connections": 120
    }
    return json.dumps(info,indent=2)


if __name__ == "__main__":
    mcp.run(transport='http',host='0.0.0.0',port=8000)
