from app.model import *

class MedicalRecordsService():
    def __init__(self, session):
        self.session = session

    def create(self, patient_id, date_of_visit, diagnosis):
        new_medicalrecords = MedicalRecords(patient_id, date_of_visit, diagnosis)
        self.session.add(new_medicalrecords)
        self.session.commit()
        return new_medicalrecords
        
    def edit(self, id, date_of_visit=None, diagnosis=None):
        medicalrecords = self.session.query(MedicalRecords).filter(MedicalRecords.id == id).first()
        if date_of_visit:
            medicalrecords.date_of_visit = date_of_visit
        if diagnosis:
            medicalrecords.diagnosis = diagnosis
        self.session.commit()
        return medicalrecords

    def delete(self, id):
        medicalrecords = self.session.query(MedicalRecords).filter(MedicalRecords.id == id).first()
        self.session.delete(medicalrecords)
        self.session.commit()

    def get(self):
        db = self.session.query(MedicalRecords).all()
        list_db = []
        for medicalrecords in db:
            medicalrecords_dict = {
            'medicalrecords': medicalrecords.to_json()
            }
            list_db.append(medicalrecords_dict)
        return list_db