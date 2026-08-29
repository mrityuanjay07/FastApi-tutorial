from fastapi import FastAPI
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