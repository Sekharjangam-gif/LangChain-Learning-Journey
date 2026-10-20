#building the ai powered applications using the streamlit
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage,AIMessage,SystemMessage
from dotenv import load_dotenv
import streamlit as st 

st.header("AI Powered Chat Based Application")

load_dotenv()
model=ChatOpenAI()

if "messages" not in st.session_state:
    st.session_state.messages=[]
    
    
for msg in st.session_state.messages:
    if isinstance(msg,HumanMessage):
        st.chat_message('user').write(msg.content)
    elif isinstance(msg,AIMessage):
        st.chat_message('ai').write(msg.content)
        
user_input=st.chat_input("Ask Anything to the AI....")

if user_input:
    if user_input=='exit'.lower():
        st.warning("You typed exit. Refresh the page to start a new chat.")
    else:
        st.chat_message('user').write(user_input)
        st.session_state.messages.append(HumanMessage(content=user_input))
        
        with st.spinner("thinking...."):
            results=model.invoke(st.session_state.messages)
            st.chat_message('ai').write(results.content)
            st.session_state.messages.append(AIMessage(content=results.content))