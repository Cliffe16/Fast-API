from fastapi import FastAPI, Depends, HTTPException 
from sqlalchemy.orm import Session
from typing import List
import models, schemas, crud 
from database import engine, get_db 

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Patient Tracker", 
              description="Tracks patients' records with FastAPi",
              version="1.0.0")

@app.post("/patients/", response_model = schemas.PatientResponse)
def create_patient(patient: schemas.PatientCreate, db: Session = Depends(get_db)):
    """Adds new patient records"""
    return crud.create_patient(db, patient)

@app.get("/patients/", response_model = List[schemas.PatientResponse])
def get_patients(db: Session = Depends(get_db)): 
    """Retrievs patients' records"""
    return crud.get_patients(db)

@app.get("/patients/{patient_id}", response_model = schemas.PatientResponse)
def get_patient(patient_id: int, db:Session = Depends(get_db)):
    """retrieves a singl patients reords"""
    patient = crud.get_patient(db, patient_id)
    if not patient:
        raise HTTPException(404, "Patient not found")
    return patient


@app.put("/patient/{patient_id}", response_model = schemas.PatientResponse)
def update_patient(patient_id: int, data: schemas.PatientUpdate, 
                   db: Session = Depends(get_db)):
    """UPdates a ppateint's records"""
    updated_patient = crud.update_patient(db, patient_id, data)
    if not updated_patient:
        raise HTTPException(404, "Patient already recorded")
    return updated_patient

@app.delete("/patients/{patient_id}")
def delete_patient(patient_id: int, db: Session = Depends(get_db)):
    """Deletes a patient'srecords"""
    patient= crud.delete_patient(db, patient_id)
    if not patient:
        raise HTTPException(404, "Patient not found")
    return {"message": "Patient deleted successfully"}
