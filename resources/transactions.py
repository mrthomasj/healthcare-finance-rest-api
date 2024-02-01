from flask_restful import Resource
from models import transactions


class Transactions(Resource):
    def get(self):
        return transactions.get_all()
