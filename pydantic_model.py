

from pydantic import BaseModel, EmailStr, AnyUrl,Field

class patient(BaseModel):
    name: str = Field(min_length=3, max_length=50)
    email: EmailStr
    linkdin: AnyUrl
    city: str
    age: int = Field(gt=0,lt=120)
    gender: str
    height: float= Field(gt=0)
    weight: float = Field(gt=0)
    bmi: float
    verdict: str

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

patient_info = {'name': 'mrityuanjay kewat','email': 'abc@gmail.com','linkdin':'https://www.linkedin.com/in/mrityuanjay-kewat', 'city': 'mumbai', 'age': 30, 'gender': 'male', 'height': 175.0, 'weight': 70.0, 'bmi': 22.86, 'verdict': 'healthy'}
patient1 = patient(**patient_info)
insert_patient(patient1)