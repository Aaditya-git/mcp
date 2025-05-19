import uv
import psycopg2
import json
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("postgres_demo")

@mcp.tool()
def connect(sql_query):
    host = "localhost"
    database = "postgres"
    user = "postgres"
    password = "postgres"
    port = 5432

    conn = None
    cursor = None
    try:
        conn = psycopg2.connect(
            dbname=database,
            user=user,
            password=password,
            host=host,
            port=port
        )
        print("connected")
        cursor = conn.cursor()
        print(f"executing sql_query: {sql_query}")
        cursor.execute(sql_query) 
        rows = cursor.fetchall()
        return json.dumps(rows, indent=2)
    finally:
        if cursor is not None:
            cursor.close()
        if conn is not None:
            conn.close()
            print("conn is closed")

if __name__ == "__main__":
    mcp.run(transport="stdio")
    print("starting the server")
