from app.model import *

class PrescriptionsService():
    def __init__(self, session):
        self.session = session

    def create(self, patient_id, date_of_prescription):
        new_prescriptions = Prescriptions(patient_id, date_of_prescription)
        self.session.add(new_prescriptions)
        self.session.commit()
        return new_prescriptions
    
    def edit(self, id, date_of_prescription=None):
        prescriptions = self.session.query(Prescriptions).filter(Prescriptions.id == id).first()
        if date_of_prescription:
            prescriptions.date_of_prescription = date_of_prescription
        self.session.commit()
        return prescriptions

    def delete(self, id):
        prescriptions = self.session.query(Prescriptions).filter(Prescriptions.id == id).first()
        self.session.delete(prescriptions)
        self.session.commit()

    def get(self):
        db = self.session.query(Prescriptions).all()
        list_db = []
        for prescriptions in db:
            prescriptions_dict = {
            'prescriptions': prescriptions.to_json()
            }
            list_db.append(prescriptions_dict)
        return list_db