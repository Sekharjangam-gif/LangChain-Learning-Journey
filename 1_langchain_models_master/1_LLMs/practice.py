from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

llm=OpenAI(model='gpt-3.5-turbo-instruct')
chat=llm.invoke("how many states are the in india according to the 2010")

print(f"LLM responce :{chat}")

