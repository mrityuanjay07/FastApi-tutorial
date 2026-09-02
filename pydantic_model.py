

from pydantic import BaseModel, EmailStr, AnyUrl,Field, field_validator,model_validator,computed_field
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
    # bmi: float = Field(gt=0)
    verdict: str
    allergies:Annotated[Optional[List[str]], Field(default=None,)]
    contact_details: List[Dict[str,str]]

    @field_validator('email')
    @classmethod
    def validate_email(cls,value):
        valid_domains=['gmail.com', 'yahoo.com', 'outlook.com']
        domain_name = value.split('@')[-1]

        if domain_name not in valid_domains:
            raise ValueError('invalid email domain, please use a valid email domain')
        return value

    @field_validator('name')
    @classmethod
    def validate_name(cls,value):
        return value.upper()

    @model_validator(mode='after')
    def validate_number(cls, model):
        if model.age>60 and 'emergency' not in model.contact_details:
            raise ValueError('emergency contact is required for patient above 60 years of age')
        return model  
    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight/((self.height/100)**2), 2)
        return bmi

def insert_patient(patient: patient):
    print(f"name: {patient.name}")
    print(f"city: {patient.city}")
    print(f"age: {patient.age}")
    print(f"gender: {patient.gender}")
    print(f"height: {patient.height}")
    print(f"weight: {patient.weight}")
    print(f"bmi: {patient.bmi}")
    print(f"verdict: {patient.verdict}")
    print(f"allergies: {patient.allergies}")
    print(f"contact_details: {patient.contact_details}")
    print(f"email: {patient.email}")
    print(f"linkdin: {patient.linkdin}")

def update_patient(patient: patient):
    print(f"name: {patient.name}")
    print(f"city: {patient.city}")
    print(f"age: {patient.age}")
    print(f"gender: {patient.gender}")
    print(f"height: {patient.height}")
    print(f"weight: {patient.weight}")
    print(f"bmi: {patient.bmi}")
    print(f"verdict: {patient.verdict}")
    print(f"allergies: {patient.allergies}")
    print(f"contact_details: {patient.contact_details}")
    print(f"email: {patient.email}")
    print(f"linkdin: {patient.linkdin}")
    

patient_info = {'name': 'mrityuanjay kewat',
                'email': 'abc@gmail.com',
                'linkdin':'https://www.linkedin.com/in/mrityuanjay-kewat',
                'city': 'mumbai',
                'age': 46,
                'gender': 'male',                      
                'height': 175.0,
                'weight': 45,
                # 'bmi': 22.86,
                'verdict': 'healthy',
                'allergies': None,
                'contact_details':[{'phone': '1234567890','emergency': '78577887', 'address': '123 Main St, Mumbai'}]}
                
patient1 = patient(**patient_info)
insert_patient(patient1)