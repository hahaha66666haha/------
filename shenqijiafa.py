from mcp.server.fastmcp import FastMCP


mcp = FastMCP("shenqijiafa")

@mcp.tool()
def shenqijiafa(age: int) -> int:
    result = age + age
    return result

if __name__ == "__main__":
    mcp.run()