from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
# chat template 1
chat_template = ChatPromptTemplate([
    ('system','You are a helpful customer support agent'),
    MessagesPlaceholder(variable_name='chat_history'),
    ('human','{query}')])

chat_history = []
# load chat history
with open('chat_history.txt') as f:
    chat_history.extend(f.readlines())

print(chat_history)

# create prompt
prompt = chat_template.invoke({'chat_history':chat_history, 'query':'Where is my refund'})

#here we are sending the prompt to llm just we are printing before sending prompt to the llm , here
# we just learning how we need to coonect the history to the llm 
print(prompt)