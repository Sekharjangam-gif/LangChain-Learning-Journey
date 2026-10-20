from langchain_core.prompts import PromptTemplate
import json
from langchain_core.load import dumpd


templat=PromptTemplate(template="""You will be give by the some cartoon charecters with names like {charecter1},
               {charecter2},{charecter3} using these charecters you need to make a story""",
               
               input_variables=["charecter1","charecter2","charecter3"],
               validate_template=True)
template_dict=dumpd(templat)

with open("template10.json","w") as f:
    json.dump(template_dict, f, indent=4)