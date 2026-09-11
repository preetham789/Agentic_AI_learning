from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Weather")

@mcp.tool()
async def get_weather(location:str) -> str:
    """Get the weather in a city."""
    return f"The weather in {location} is sunny."

#transport = "streamable_http" means that the mcp server will communicate with the client using streamable http.
#dev = True means that the server will be in debug mode.
#debug = True means that the server will be in debug mode.
#port = 5001 means that the server will be running on port 5001.
#host = "[IP_ADDRESS]" means that the server will be running on localhost.

if __name__ == "__main__":
    mcp.run(transport="streamable-http") 