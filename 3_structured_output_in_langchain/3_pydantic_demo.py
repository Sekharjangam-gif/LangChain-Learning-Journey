from pydantic import BaseModel, EmailStr, Field
from typing import Optional


###################3 first example
# class Student(BaseModel):
#     name : str
    
# #new_student=({"name":"sekhar"})

# new_student=({"name":32})

# student=Student(**new_student)
# print(student)
# print(type(student))


class Student(BaseModel):

    name: str = 'nitish'
    age: Optional[int] = None
    email: EmailStr
    cgpa: float = Field(gt=0, lt=10, default=5, description='A decimal value representing the cgpa of the student')


new_student = {'age':'32', 'email':'abc@gmail.com'}

student = Student(**new_student)

#converting the pydantic obect into python dict
student_dict = dict(student)
print(student_dict['age'])
#converting the pydantic obect into python json 
student_json = student.model_dump_json()