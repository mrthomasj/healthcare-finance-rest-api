from flask_restful import Resource
from models import patients


class Patients(Resource):

    def get(self):
        return patients.get_all()
