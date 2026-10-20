from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

# Initialize the model
model = ChatOpenAI()

st.header("Chatbot Application")

# 1. Initialize session state to store the chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# 2. Display all previous messages on the screen
for msg in st.session_state.messages:
    if isinstance(msg, HumanMessage):
        st.chat_message("user").write(msg.content)
    elif isinstance(msg, AIMessage):
        st.chat_message("assistant").write(msg.content)

# 3. Get user input (st.chat_input is better for chatbots than text_input)
user_input = st.chat_input("Enter your message here...")

if user_input:
    if user_input.lower() == 'exit':
        st.warning("You typed exit. Refresh the page to start a new chat.")
    else:
        # Display the user's new message immediately
        st.chat_message("user").write(user_input)
        
        # Add user message to history
        st.session_state.messages.append(HumanMessage(content=user_input))
        
        # Call the model with the full history so it remembers context
        with st.spinner("Thinking..."):
            results = model.invoke(st.session_state.messages)
            
        # Display AI response
        st.chat_message("assistant").write(results.content)
        
        # Add AI response to history
        st.session_state.messages.append(AIMessage(content=results.content))