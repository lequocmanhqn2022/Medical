from app.model import *
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

class ListMedication(Base):
    __tablename__ = "list_medication_table"
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_prescription = Column(ForeignKey('prescriptions_table.id'))
    id_medication = Column(ForeignKey('medications_table.id'))
    quantity = Column(Integer)
    instructions = Column(String(255))
    prescriptions = relationship("Prescriptions", back_populates='list_medical')
    medication = relationship("Medications", back_populates='list_medical')

    def __init__(self, id_prescription, id_medication, quantity, instructions):
        self.id_prescription = id_prescription
        self.id_medication = id_medication
        self.quantity = quantity
        self.instructions = instructions
    
    def to_json(self):
        return {
            "prescriptions": self.prescriptions.to_json(),
            "medication": self.medication.to_json(),
            "quantity": self.quantity,
            "instructions": self.instructions
        }