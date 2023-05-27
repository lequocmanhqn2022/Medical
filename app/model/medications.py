from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.model import *

class Medications(Base):
    __tablename__ = 'medications_table'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255))
    description = Column(String(255))
    instructions = Column(String(255))
    list_medical = relationship("ListMedication", back_populates='medication')

    def __init__(self, name, description, instructions):
        self.name = name
        self.description = description
        self.instructions = instructions
    
    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "instructions": self.instructions
        }