from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


"""
1.we will take the prompt for the user
2.invoke to the model
3.then we will get the output from the llm
"""

load_dotenv()

prompt = PromptTemplate(
    template='Generate 5 interesting facts about {topic}',
    input_variables=['topic']
)

model = ChatOpenAI()

parser = StrOutputParser()

chain = prompt | model | parser

result = chain.invoke({'topic':'cricket'})

print(result)


##using the below step we can get the chain graph which we used in our stage by calling these below
chain.get_graph().print_ascii()