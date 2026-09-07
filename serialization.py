from pydantic import BaseModel

class Address(BaseModel):
    street:str
    city:str
    state:str
    pincode:str

class patient(BaseModel):
    name: str
    age: int
    address: Address

address_dict={
    'street':'beemagram',
    'city':'kotma',
    'state':'mp',
    'pincode':'481701'
}
address1 = Address(**address_dict)

patient_dict = {
    'name':'anku',
    'age': 19, 
    'address':address1  
}
patient1 = patient(**patient_dict)
print(patient1)
print(patient1.name)
print(patient1.address.city)
print(patient1.address.pincode)

temp = patient1.model_dump()
print(temp)
print(type(temp))

temp1 = patient1.model_dump_json()
print(temp1)
print(type(temp1))