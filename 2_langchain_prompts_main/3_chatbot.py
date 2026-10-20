from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

###################
#SIMPLE CHAT BOT

# while True:
#     user_input = input('You: ')
#     if user_input == 'exit':
#         break
#     results=model.invoke(user_input)
#     print("AI: ",results.content)

#by doing above ai doest not have the history so using below line we can add the history


####################################
#ADDING THE CHAT HISTORY

# chat_history = [
#     SystemMessage(content='You are a helpful AI assistant')]

# while True:
#     user_input = input('You: ')
#     chat_history.append(user_input)
#     if user_input == 'exit':
#         break
#     result = model.invoke(chat_history)
#     chat_history.append(content=result.content)
#     print("AI: ",result.content)

# print(chat_history)

####ADDING THE CHAT HOSTORY WITH USERS AND AI WITH CHARECTERS
chat_history = [
    SystemMessage(content='You are a helpful AI assistant')]

while True:
    user_input = input('You: ')
    chat_history.append(HumanMessage(content=user_input))
    if user_input == 'exit':
        break
    result = model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    print("AI: ",result.content)

print(chat_history)