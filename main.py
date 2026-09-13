
from fastapi import FastAPI, Path,HTTPException,Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel,Field,computed_field
from typing import Literal, Optional,Dict,List,Annotated
import json


app = FastAPI()

class Patient(BaseModel):
    id: Annotated[str, Field(min_length=3, max_length=10, title="Patient ID", description="This field is required and should be between 3 and 10 characters",example="P001")]
    name: Annotated[str, Field(min_length=2, max_length=100, title="Patient Name", description="This field is required and should be between 2 and 100 characters",example="John Doe")]
    city: Annotated[str, Field(min_length=2, max_length=100, title="Patient City", description="This field is required and should be between 2 and 100 characters",example="New York")]
    age: Annotated[int, Field(gt=0, title="Patient Age", description="This field is required and should be a positive integer",example=30)]
    height: Annotated[float, Field(gt=0, title="Patient Height", description="This field is required and should be a positive float",example=175.5)]
    weight: Annotated[float, Field(gt=0, title="Patient Weight", description="This field is required and should be a positive float",example=70.0)]

class patientupdate(BaseModel):
    name: Annotated[Optional[str], Field(default = None)]
    city:Annotated[Optional[str],Field(default=None)]
    age:Annotated[Optional[int],Field(default=None)]
    gender:Annotated[Optional[Literal['male','female']],Field(default=None)]
    height:Annotated[Optional[float],Field(default=None)]
    weight:Annotated[Optional[float],Field(default=None)]
  


    @computed_field
    @property
    def bmi(self) -> float:
        if self.height is None or self.weight is None:
            return None
        bmi = round(self.weight/((self.height/100)**2),2)
        return bmi
    @computed_field
    @property
    def verdict(self) -> str:
        if self.bmi is None:
            return "Invalid BMI"
        if self.bmi < 18.5:
            return "Underweight"
        elif 18.5 <= self.bmi < 24.9:
            return "Normal weight"
        elif 25 <= self.bmi < 29.9:
            return "Overweight"
        else:
            return "Obesity"

def load_data():
    with open("patient.json", "r") as f:
        data = json.load(f)
    return data
def save_data(data):
    with open('patient.json', 'w') as f:
        json.dump(data, f)

@app.get("/")
def hello():
    return {"message": "patient Management System Api"}

@app.get("/about")
def about():
    return {"message": "This is fully functional pattient management system api which can be used to manage patient data and their health records."}

@app.get("/view")
def view():
    data = load_data()
    return data

@app.get("/patient_id/{patient_id}")
def patient_id(patient_id: str = Path(..., description = 'Enter the patient id to get the details of the patient', example = "P001")):
    data = load_data()

    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404,detail='patient not found')

@app.get("/sort")
def sort_patients(sort_by: str = Query(..., description = 'Enter the field to sort the patients on the basis of height, weight, or bmi'), order:str = Query('asc', description = 'Enter the order of sorting, either asc or desc')):
    data = load_data()
    if sort_by not in ['height', 'weight', 'bmi']:
        raise HTTPException(status_code= 400, detail= 'invalid sort field, please choose from height, weight or bmi')
    if order not in ['asc', 'desc']:
        raise HTTPException(status_code = 400, detail= 'invalid order, please choose either asc or desc')
    sorted_data = sorted(data.values(), key=lambda x: x[sort_by], reverse=(order == 'desc'))
    return sorted_data

@app.post('/create')
def create_patient(patient: Patient):

    data = load_data()

    if patient.id in data:
        raise HTTPException(status_code=400, detail='patient already exists')

    data[patient.id] = patient.model_dump(exclude={'id'})
    save_data(data)

    return JSONResponse(status_code=201, content={'message': 'patient created successfully'})

@app.put('/update/{patient_id}')
def update_patient(patient_id:str, patient_update: patientupdate):
    data = load_data()

    if patient_id not in data:
        raise HTTPException(status_code = 404, detail='patient not found')

    existing_patient_info = data[patient_id]

    updated_patient_info = patient_update.model_dump(exclude_unset=True)

    for key, value in updated_patient_info.items():
        existing_patient_info[key] = value

    existing_patient_info['id'] = patient_id
    patient_pydantic_obj = Patient(**existing_patient_info)

    existing_patient_info = patient_pydantic_obj.model_dump(exclude='id')

    data[patient_id] = existing_patient_info
    save_data(data)

    return JSONResponse(status_code=200, content={'message': 'patient updated successfully'})

@app.delete('/delete/{patient_id}')
def delete_patient(patient_id:str):
    data = load_data()

    if patient_id not in data:
        raise HTTPException(status_code=404, detail='patient not found')

    del data[patient_id]

    save_data(data)

    return JSONResponse(status_code=200, content={'message':'patient deleted sucessfully'})