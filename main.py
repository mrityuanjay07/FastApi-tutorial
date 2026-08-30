from fastapi import FastAPI, Path,HTTPException,Query
import json
app = FastAPI()

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