from app.conn import Database
from flask import Blueprint, jsonify, request
import json
from app.service.medicalRecordsService import MedicalRecordsService

class MedicalRecordsController():
    def __init__(self):
        self.api_medicalRecords = Blueprint('api_medicalRecords',__name__)
        self.session = Database().get_session()
        self.medicalrecords_service = MedicalRecordsService(self.session)

        @self.api_medicalRecords.route('/medicalrecords', methods = ["GET"])
        def get():
            try:
                response = self.medicalrecords_service.get()
                return jsonify(response)
            except ValueError as e:
                return jsonify({'message': str(e)})
            
        @self.api_medicalRecords.route('/medicalrecords/<int:id>', methods = ["POST"])
        def create(id):
            medicalrecords = request.json['medicalrecords']
            date_of_visit = medicalrecords['date_of_visit']
            diagnosis = medicalrecords['diagnosis']
            try:
                new_medicalrecords = self.medicalrecords_service.create(id, date_of_visit, diagnosis)
                response = jsonify({'message': 'Add medicalrecords success!', "medicalrecords": new_medicalrecords.to_json()})
                return response
            except ValueError as e:
                return jsonify({'message': str(e)})

        @self.api_medicalRecords.route('/medicalrecords/<int:id>', methods = ["PUT"])
        def edit(id):
            try:
                medicalrecords = request.json['medicalrecords']
                date_of_visit = medicalrecords['date_of_visit']
                diagnosis = medicalrecords['diagnosis']
                update = self.medicalrecords_service.edit(id, date_of_visit, diagnosis)
                return {"message": "Update medicalrecords successfully", "medicalrecords": update.to_json()}
            except ValueError as e:
                return {"error": str(e)}

        @self.api_medicalRecords.route('/medicalrecords/<int:id>', methods = ["DELETE"])
        def delete(id):
            self.medicalrecords_service.delete(id)
            response = jsonify({'message': 'Deleted successfully'})
            return response