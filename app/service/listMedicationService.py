from app.model import *

class ListMedicationService():
    def __init__(self, session):
        self.session = session

    def create(self, id_prescription, id_medication, quantity, instructions):
        new_list = ListMedication(id_prescription, id_medication, quantity, instructions)
        self.session.add(new_list)
        self.session.commit()
    
    def edit(self, id_medication=None, quantity=None, instructions=None):
        list = self.session.query(ListMedication).filter(ListMedication.id == id).first()
        if id_medication:
            list.id_medication = id_medication
        if quantity:
            list.quantity = quantity
        if instructions:
            list.instructions = instructions
        return list

    def delete(self, id_prescription):
        list = self.session.query(ListMedication).filter(ListMedication.id_prescription == id_prescription).all()
        for i in list:
            self.session.delete(i)
            self.session.commit()
    
    def get_byID(self, id):
        db = self.session.query(ListMedication).filter(ListMedication.id_prescription == id).all()
        list_db = []
        for list_medication in db:
            list_medication_dict = {
            'medication': list_medication.to_json()
            }
            list_db.append(list_medication_dict)
        return list_db