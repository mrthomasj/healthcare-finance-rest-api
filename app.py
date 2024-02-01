from flask import Flask
from flask_restful import Api
from resources.patients import Patients
from resources.pharmacies import Pharmacies
from resources.transactions import Transactions

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///backend_test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)

api.add_resource(Patients, '/patients')
api.add_resource(Pharmacies, '/pharmacies')
api.add_resource(Transactions, '/transactions')

if __name__ == '__main__':
    from database.services.service import db
    db.init_app(app)
    app.run(debug=True)
