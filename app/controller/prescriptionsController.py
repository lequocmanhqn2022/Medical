from app.conn import Database
from flask import Blueprint, jsonify, request
import json
from app.service.prescriptionsService import PrescriptionsService
from app.service.listMedicationService import ListMedicationService

class PrescriptionsController():
    def __init__(self):
        self.api_prescriptions = Blueprint('api_prescriptions',__name__)
        self.session = Database().get_session()
        self.prescriptions_service = PrescriptionsService(self.session)
        self.list_medication_service = ListMedicationService(self.session)

        @self.api_prescriptions.route('/prescriptions', methods = ["GET"])
        def get():
            try:
                response = self.prescriptions_service.get()
                return jsonify(response)
            except ValueError as e:
                return jsonify({'message': str(e)})
            
        @self.api_prescriptions.route('/prescriptions/<int:id>', methods = ["POST"])
        def create(id):
            prescriptions = request.json['prescriptions']
            date_of_prescription = prescriptions['date_of_prescription']
            list_medication = request.json['list_medication']   
            medication_id = list_medication['medication_id']
            quantity = list_medication['quantity']
            instructions = list_medication['instructions']
            try:
                new_prescription = self.prescriptions_service.create(id, date_of_prescription)
                self.list_medication_service.create(new_prescription.id, medication_id, quantity, instructions)
                response = jsonify({'message': 'Add prescriptions success!'})
                return response
            except ValueError as e:
                return jsonify({'message': str(e)})

        @self.api_prescriptions.route('/prescriptions/<int:id>', methods = ["PUT"])
        def edit(id):
            try:
                prescriptions = json.loads(request.form["prescriptions"])
                date_of_prescription = prescriptions['date_of_prescription']
                medication_id = prescriptions['medication_id']
                quantity = prescriptions['quantity']
                instructions = prescriptions['instructions']
                update_date = self.prescriptions_service.edit(id, date_of_prescription)
                self.list_medication_service.edit(medication_id, quantity, instructions)
                return {"message": "Update prescriptions successfully", "prescriptions": update_date.to_json()}
            except ValueError as e:
                return {"error": str(e)}

        @self.api_prescriptions.route('/prescriptions/<int:id>', methods = ["DELETE"])
        def delete(id):
            self.list_medication_service.delete(id)
            self.prescriptions_service.delete(id)
            response = jsonify({'message': 'Deleted successfully'})
            return response