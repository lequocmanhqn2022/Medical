from flask import Flask
from app.controller import *
from flask_cors import CORS

class App(Flask):
    def __init__(self, import_name):
        super().__init__(import_name)
        self._configure_cors()
        self._register_controllers()
    
    def _configure_cors(self):
        CORS(self, supports_credentials=True)

    def _register_controllers(self):
        self.register_blueprint(PatientsController().api_patients)
        self.register_blueprint(MedicalRecordsController().api_medicalRecords)
        self.register_blueprint(PrescriptionsController().api_prescriptions)
        self.register_blueprint(MedicationsController().api_medications)