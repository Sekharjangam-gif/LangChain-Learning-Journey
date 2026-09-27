from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
# if we want to use huuging face models using the api we need to use the huggingfaceendpoint also
from dotenv import load_dotenv

load_dotenv()

#hugging face 
llm1= HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation"
)
# Change the repo_id to a supported model
llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Meta-Llama-3-8B-Instruct", 
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

result = model.invoke("What is the capital of India")

print(result.content)