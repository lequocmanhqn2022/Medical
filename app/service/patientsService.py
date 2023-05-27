from app.model import *
from sqlalchemy import desc

class PatientsService():
    def __init__(self, session):
        self.session = session

    def create(self, name, address, phone, birthday, gender):
        check = self.session.query(Patients).filter(Patients.name == name, Patients.address == address, Patients.phone == phone, Patients.birthday == birthday).first()
        if check:
            raise ValueError('Patients already exists')
        new_patients = Patients(name, address, phone, birthday, gender)
        self.session.add(new_patients)
        self.session.commit()
        return new_patients
    
    def edit(self, id, name=None, address=None, phone=None, birthday=None, gender=None):
        patients = self.session.query(Patients).filter(Patients.id == id).first()
        if name:
            patients.name = name
        if address:
            patients.address = address
        if phone:
            patients.phone = phone
        if birthday:
            patients.birthday = birthday
        if gender:
            patients.gender = gender
        self.session.commit()
        return patients

    def delete(self, id):
        patients = self.session.query(Patients).filter(Patients.id == id).first()
        self.session.delete(patients)
        self.session.commit()


    def get(self):
        db = self.session.query(Patients).order_by(desc(Patients.id)).all()
        list_db = []
        for patient in db:
            patient_dict = {
                'patient': patient.to_json()
            }
            list_db.append(patient_dict)
        return list_db

    def get_byID(self, id):
        db = self.session.query(Patients).filter(Patients.id == id).first()
        return db