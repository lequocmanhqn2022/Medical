from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.orm import relationship
from app.model import *
from datetime import datetime as dt

class Patients(Base):
    __tablename__ = 'patients_table'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255))
    address = Column(String(255))
    phone = Column(String(20))
    birthday = Column(Date)
    gender = Column(String(10))
    medicalRecords = relationship("MedicalRecords", back_populates="patients")
    prescriptions = relationship("Prescriptions", back_populates="patients")

    def __init__(self, name, address, phone, birthday, gender):
        self.name = name
        self.address = address
        self.phone = phone
        self.set_birthday(birthday)
        self.gender = gender
    
    def set_birthday(self, birthday_str):
        birthday_datetime = dt.strptime(birthday_str, "%Y-%m-%d")
        birthday_date = birthday_datetime.date()
        self.birthday = birthday_date
    
    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "address": self.address,
            "phone": self.phone,
            "birthday": self.birthday.strftime("%Y-%m-%d"),
            "gender": self.gender
        }