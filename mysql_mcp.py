from mcp.server.fastmcp import FastMCP
import pymysql

mcp = FastMCP("MySQLMCP")

@mcp.tool()
def analysis_data(age: int) -> int:
    conn = pymysql.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="123456",
        database="mcp"
    )
    cursor = conn.cursor()
    cursor.execute(f"SELECT COUNT(*) FROM user where age > {age}")
    result = cursor.fetchone()[0]
    cursor.close()
    conn.close()
    return result

if __name__ == "__main__":
    mcp.run()