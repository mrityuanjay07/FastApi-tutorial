

from pydantic import BaseModel, EmailStr, AnyUrl,Field
from typing import Optional,Dict,List,Annotated

class patient(BaseModel):
    name: Annotated[str, Field(min_length=3, max_length=50, title="Name of the patient", description="This field is required and should be between 3 and 50 characters",example="ram kumar")]
    email: EmailStr
    linkdin: AnyUrl
    city: str
    age: int = Field(gt=0,lt=120)
    gender: str
    height: float= Field(gt=0)
    weight:Annotated[float, Field(gt=0, strict=True)]
    bmi: float = Field(gt=0)
    verdict: str
    allergies:Annotated[Optional[List[str]], Field(default=None,)]
    contact_details: List[Dict[str,str]]

def insert_patient(patient: patient):
    print(patient.name)
    print(patient.city)
    print(patient.age)
    print(patient.gender)
    print(patient.height)
    print(patient.weight)
    print(patient.bmi)
    print(patient.verdict)

def update_patient(patient: patient):
    print(patient.name)
    print(patient.city)
    print(patient.age)
    print(patient.gender)
    print(patient.height)
    print(patient.weight)
    print(patient.bmi)
    print(patient.verdict)

patient_info = {'name': 'mrityuanjay kewat','email': 'abc@gmail.com','linkdin':'https://www.linkedin.com/in/mrityuanjay-kewat', 'city': 'mumbai', 'age': 30, 'gender': 'male', 'height': 175.0, 'weight': 45, 'bmi': 22.86, 'verdict': 'healthy','allergies': None,'contact_details':[{'phone': '1234567890', 'address': '123 Main St, Mumbai'}]}
                
patient1 = patient(**patient_info)
insert_patient(patient1)