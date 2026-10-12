from httpx import stream
from langgraph.graph import StateGraph, START, END
from typing import TypedDict, Annotated
from langchain_core.messages import BaseMessage, trim_messages
from langchain_groq import ChatGroq
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.graph.message import add_messages

from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

llm = ChatGroq(model="openai/gpt-oss-120b", max_tokens=1024)

class ChatState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]

def chat_node(state:ChatState):
    message = trim_messages(
        state['messages'],
        max_tokens=5000,
        token_counter="approximate",
        strategy="last",
        start_on="human",
        include_system=True,
    )
    response = llm.invoke(message)
    return {'messages':[response]}

checkpoint = InMemorySaver()

graph = StateGraph(ChatState)
graph.add_node('chat', chat_node)
graph.add_edge( START, 'chat')
graph.add_edge('chat', END)

chatbot = graph.compile(checkpointer=checkpoint)


                                 
