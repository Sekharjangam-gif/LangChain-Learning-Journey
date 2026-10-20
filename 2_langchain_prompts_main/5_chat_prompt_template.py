from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage


###############################
#first chat history

# chat_template = ChatPromptTemplate([
#     SystemMessage(content='You are a helpful {domain} expert'),
#     HumanMessage(content='Explain in simple terms, what is {topic}')
# ])

# prompt = chat_template.invoke({'domain':'cricket','topic':'Dusra'})
# #### we will not the correct output we need to change chat_template
# print(prompt)

##########################################
##this is below is the proper way to save the message using this chat_template , like dynamic set of message

chat_template = ChatPromptTemplate([
    ('system', 'You are a helpful {domain} expert'),
    ('human', 'Explain in simple terms, what is {topic}')
])

prompt = chat_template.invoke({'domain':'cricket','topic':'Dusra'})

print(prompt)