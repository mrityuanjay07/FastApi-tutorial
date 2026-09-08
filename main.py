from fastapi import FastAPI, Path,HTTPException,Query
from pydantic import BaseModel,Field,computed_field
from typing import Optional,Dict,List,Annotated
import json
app = FastAPI()

class Patient(BaseModel):
    id: Annotated[str, Field(min_length=3, max_length=10, title="Patient ID", description="This field is required and should be between 3 and 10 characters",example="P001")]
    name: Annotated[str, Field(min_length=2, max_length=100, title="Patient Name", description="This field is required and should be between 2 and 100 characters",example="John Doe")]
    age: Annotated[int, Field(gt=0, title="Patient Age", description="This field is required and should be a positive integer",example=30)]
    height: Annotated[float, Field(gt=0, title="Patient Height", description="This field is required and should be a positive float",example=175.5)]
    weight: Annotated[float, Field(gt=0, title="Patient Weight", description="This field is required and should be a positive float",example=70.0)]
    bmi: Annotated[float, Field(gt=0, title="Patient BMI", description="This field is required and should be a positive float",example=22.5)]

    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight/((self.height/100)**2),2)
        return bmi
    @computed_field
    @property
    def verdict(self) -> str:
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

