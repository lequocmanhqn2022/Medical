from sqlalchemy import Column, Date, ForeignKey, Integer
from sqlalchemy.orm import relationship
from app.model import *
from datetime import datetime as dt

class Prescriptions(Base):
    __tablename__ = 'prescriptions_table'
    id = Column(Integer, primary_key=True, autoincrement=True)
    patient_id = Column(ForeignKey('patients_table.id'))
    date_of_prescription = Column(Date)
    patients = relationship("Patients", back_populates='prescriptions')
    list_medical = relationship("ListMedication", back_populates='prescriptions')

    def __init__(self, patient_id, date_of_prescription):
        self.patient_id = patient_id
        self.set_date_of_prescription(date_of_prescription)
    
    def set_date_of_prescription(self, day_str):
        day_datetime = dt.strptime(day_str, "%Y-%m-%d")
        day_date = day_datetime.date()
        self.date_of_prescription = day_date
    
    def to_json(self):
        return {
            "id": self.id,
            "patient_id": self.patients.to_json(),
            "date_of_prescription": self.date_of_prescription.strftime("%Y-%m-%d")
        }