# from mcp.server.fastmcp import FastMCP
from mcp.server import MCPServer

mcp = MCPServer("calculator")
#  mcp = FastMCP("calculator") 
@mcp.tool()
def add(a: int, b: int) -> int:
    return a + b

@mcp.tool()
def subtract(a: int, b: int) -> int:
    return a - b

@mcp.tool()
def multiply(a: int, b: int) -> int:
    return a * b

if __name__ == "__main__":
    mcp.run()

