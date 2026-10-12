import streamlit as st
from langgraph_backend import chatbot
from langchain_core.messages import HumanMessage

#st.session_state -> dict ->
CONFIG = {'configurable': {'thread_id': '1'}}  # Configuration for the chatbot

if 'messages_history' not in st.session_state:
    st.session_state['messages_history'] = []  # Initialize message history


#loading the chat history 
for message in st.session_state['messages_history']:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


user_input = st.chat_input("type here... ")  # Get user input

if user_input:
    #first add the message to the message history
    st.session_state['messages_history'].append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    
    with st.chat_message("assistant"):
        ai_message = st.write_stream(
            message_chunk.content for message_chunk,metadata in chatbot.stream(
                {'messages': [HumanMessage(content=user_input)]},
                config=CONFIG,
                stream_mode = 'messages'
            )
        )
    st.session_state['messages_history'].append({'role': 'assistant', 'content': ai_message})
