from pydantic import BaseModel

class patient(BaseModel):
    name: str
    city: str
    age: int
    gender: str
    height: float
    weight: float
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

patient_info = {'name': 'mrityuanjay kewat', 'city': 'mumbai', 'age': 30, 'gender': 'male', 'height': 175.0, 'weight': 70.0, 'bmi': 22.86, 'verdict': 'healthy'}
patient1 = patient(**patient_info)
insert_patient(patient1)