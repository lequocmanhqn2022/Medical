from app.model import *

class MedicationsService():
    def __init__(self, session):
        self.session = session
    
    def create(self, name, description, instructions):
        new_medication = Medications(name, description, instructions)
        self.session.add(new_medication)
        self.session.commit()
        return new_medication
    
    def edit(self, id, name=None, description=None, instructions=None):
        medication = self.session.query(Medications).filter(Medications.id == id).first()
        if name:
            medication.name = name
        if description:
            medication.description = description
        if instructions:
            medication.instructions = instructions
        self.session.commit()
        return medication

    def delete(self, id):
        medication = self.session.query(Medications).filter(Medications.id == id).first()
        self.session.delete(medication)
        self.session.commit()

    def get(self):
        db = self.session.query(Medications).all()
        list_db = []
        for medication in db:
            medication_dict = {
            'medication': medication.to_json()
            }
            list_db.append(medication_dict)
        return list_db