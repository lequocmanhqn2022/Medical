from app.conn import Database
from flask import Blueprint, jsonify, request
import json
from app.service.medicationsService import MedicationsService

class MedicationsController():
    def __init__(self):
        self.api_medications = Blueprint('api_medications',__name__)
        self.session = Database().get_session()
        self.medications_service = MedicationsService(self.session)

        @self.api_medications.route('/medications', methods = ["GET"])
        def get():
            try:
                response = self.medications_service.get()
                return jsonify(response)
            except ValueError as e:
                return jsonify({'message': str(e)})
            
        @self.api_medications.route('/medications', methods = ["POST"])
        def create():
            medications = request.json['medications']
            name = medications['name']
            description = medications['description']
            instructions = medications['instructions']
            try:
                new_medications = self.medications_service.create(name, description, instructions)
                response = jsonify({'message': 'Add medications success!', "medications": new_medications.to_json()})
                return response
            except ValueError as e:
                return jsonify({'message': str(e)})

        @self.api_medications.route('/medications/<int:id>', methods = ["PUT"])
        def edit(id):
            try:
                medications = request.json['medications']
                name = medications['name']
                description = medications['description']
                instructions = medications['instructions']
                update = self.medications_service.edit(id, name, description, instructions)
                return {"message": "Update medications successfully", "medications": update.to_json()}
            except ValueError as e:
                return {"error": str(e)}

        @self.api_medications.route('/medications/<int:id>', methods = ["DELETE"])
        def delete(id):
            self.medications_service.delete(id)
            response = jsonify({'message': 'Deleted successfully'})
            return response