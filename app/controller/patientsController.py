import json
from app.conn import Database
from flask import Blueprint, jsonify, request
from app.service.patientsService import PatientsService

class PatientsController():
    def __init__(self):
        self.api_patients = Blueprint('api_patients',__name__)
        self.session = Database().get_session()
        self.patient_service = PatientsService(self.session)

        @self.api_patients.route('/patients/<int:id>', methods = ["GET"])
        def get_byID(id):
            try:
                response = self.patient_service.get_byID(id)
                return jsonify(response.to_json())
            except ValueError as e:
                return jsonify({'message': str(e)})

        @self.api_patients.route('/patients', methods = ["GET"])
        def get():
            try:
                response = self.patient_service.get()
                return jsonify(response)
            except ValueError as e:
                return jsonify({'message': str(e)})
            
        @self.api_patients.route('/patients', methods = ["POST"])
        def create():
            patients = request.json['patients']
            name = patients['name']
            address = patients['address']
            phone = patients['phone']
            birthday = patients['birthday']
            gender = patients['gender']
            try:
                new_patients = self.patient_service.create(name, address, phone, birthday, gender)
                response = jsonify({'message': 'Add patients success!', "patients": new_patients.to_json()})
                return response
            except ValueError as e:
                return jsonify({'message': str(e)})
            
        @self.api_patients.route('/patients/<int:id>', methods = ["PUT"])
        def edit(id):
            try:
                patients = request.json['patients']
                name = patients['name']
                address = patients['address']
                phone = patients['phone']
                birthday = patients['birthday']
                gender = patients['gender']
                update = self.patient_service.edit(id, name, address, phone, birthday, gender)
                return {"message": "Update patients successfully", "patients": update.to_json()}
            except ValueError as e:
                return {"error": str(e)}

        @self.api_patients.route('/patients/<int:id>', methods = ["DELETE"])
        def delete(id):
            self.patient_service.delete(id)
            response = jsonify({'message': 'Patients deleted successfully'})
            return response