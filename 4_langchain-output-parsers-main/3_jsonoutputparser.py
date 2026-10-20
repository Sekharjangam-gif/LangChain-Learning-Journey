from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

# Define the model
llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

parser = JsonOutputParser()


################################ stage 1 without chains#######################

# template = PromptTemplate(
#     template='Give me the name,age and city of a fictional person \n {format_instruction}',
#     input_variables=[],
#     partial_variables={'format_instruction': parser.get_format_instructions()}
# )


# promt=template.format()


# result=model.invoke(promt)

# print(result)

# final_results=parser.parse(result.content)

# print(final_results)
# print(type(final_results))

################################ stage 2 with chains#######################


template = PromptTemplate(
    template='Give me the name,age and city of a fictional person \n {format_instruction}',
    input_variables=[],
    partial_variables={'format_instruction': parser.get_format_instructions()}
)

chain = template | model | parser

result = chain.invoke({})

print(result)


################################ stage 3 with chains with json schems #######################


template = PromptTemplate(
    template='Give me five facts about {topic} \n {format_instruction}',
    input_variables=['topic'],
    partial_variables={'format_instruction': parser.get_format_instructions()}
)

chain = template | model | parser
result = chain.invoke({'topic':'black hole'})
print(result)


### about we can not get output in schema so for that we need to user some other output parsers