from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()

import asyncio

async def main():
    client = MultiServerMCPClient(
        {
            "math":{
                "command":"python",
                "args":["MCP/mathserver.py"],
                "transport": "stdio",
            },
            "weather":{
                "url":"http://localhost:8000/mcp",#ensure that mcp server is running here
                "transport": "streamable-http",
            }

        }
    )
    import os
    os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
    tools = await client.get_tools()
    model = ChatGroq(model = "qwen/qwen3.6-27b")
    agent = create_react_agent(
        model,tools
    )

    math_response = await agent.ainvoke(
        {"messages":[{"role":"user","content":"what is (3+5) x 12"}]}
    )
    print("math_response:",math_response['messages'][-1].content)

    weather_response = await agent.ainvoke(
        {"messages":[{"role":"user","content":"what is the weather in new york?"}]}
    )
    print("weather_response:",weather_response['messages'][-1].content)

asyncio.run(main())


    
    