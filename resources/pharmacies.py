from flask_restful import Resource
from models import pharmacies


class Pharmacies(Resource):
    def get(self):
        return pharmacies.get_all()

    def post(self):
        return pharmacies.get_user()
