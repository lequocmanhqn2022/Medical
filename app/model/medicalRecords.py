from sqlalchemy import Column, Date, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from app.model import *
from datetime import datetime as dt

class MedicalRecords(Base):
    __tablename__ = 'medicalrecords_table'
    id = Column(Integer, primary_key=True, autoincrement=True)
    patient_id = Column(ForeignKey('patients_table.id'))
    date_of_visit = Column(Date)
    diagnosis =Column(String(255))
    patients = relationship("Patients", back_populates="medicalRecords")

    def __init__(self, patient_id, date_of_visit, diagnosis):
        self.patient_id = patient_id
        self.set_day(date_of_visit)
        self.diagnosis = diagnosis
    
    def set_day(self, day_str):
        day_datetime = dt.strptime(day_str, "%Y-%m-%d")
        day_date = day_datetime.date()
        self.date_of_visit = day_date
    
    def to_json(self):
        if isinstance(self.date_of_visit, str):
            self.date_of_visit = dt.strptime(self.date_of_visit, "%Y-%m-%d").date()
        
        return {
            "id": self.id,
            "patient_id": self.patients.to_json(),
            "date_of_visit": self.date_of_visit.strftime("%Y-%m-%d"),
            "diagnosis": self.diagnosis
        }
