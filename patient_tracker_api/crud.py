from sqlalchemy.orm import Session
import models, schemas

def create_patient(db: Session, patient: schemas.PatientCreate):
    """Creates a new patient record"""
    db_patient = models.Patient(**patient.model_dump())
    db.add(db_patient)
    db.commit()
    db.refresh
    return db_student

def get_patient(db: Session, patient_id: int):
    """Gets a single patient's record"""
    return db.query(models.Patient).filter(models.Patient.id == patient_id).first()

def get_patients():
    """Gets patients' records"""
    return db.query(models.Patient).all()

def update_patient(db: Session, patient_id: int, data=schemas.PatientUpdate):
    """Updates patients' records"""
    patient = db.query(models.Patient).filter(models.Patient.id == patient_id).first()

    if not patient:
        return None

    updates = data.model_dump(exclude_unset=True)
    for field, value in updates.items():
        setattr(patient, field, value)

    db.commit()
    db.refresh(patient)
    return patient

def delete_patient():
    """Deletes patients' records"""
    patient = db.query(models.Patient).filter(models.Patient.id == patient_id).first()

    if not patient:
        return None

    db.delete(patient)
    db.commit()
    return patient

