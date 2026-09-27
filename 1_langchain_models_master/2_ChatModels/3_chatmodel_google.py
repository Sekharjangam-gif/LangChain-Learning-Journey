from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

#model = ChatGoogleGenerativeAI(model='gemini-1.5-pro')
#model = ChatGoogleGenerativeAI(model="gemini-1.5-pro-latest")
# model = ChatGoogleGenerativeAI(model="gemini-flash-latest")
# result = model.invoke('What is the capital of India')

# print(result.text)



import warnings
from langchain_google_genai import ChatGoogleGenerativeAI

# Suppress the background warning messages from the Google SDK
warnings.filterwarnings("ignore")

model = ChatGoogleGenerativeAI(model="gemini-flash-latest")
result = model.invoke('What is the capital of India')

# Use .content to get exactly the text the model answered
print(result.content[0]['text'])



# import google.generativeai as genai
# import os
# from dotenv import load_dotenv

# load_dotenv()
# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# print("Models available to your API key:")
# for m in genai.list_models():
#     if 'generateContent' in m.supported_generation_methods:
#         print(m.name)