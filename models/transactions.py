from database.services.service import db
from flask import jsonify
from sqlalchemy.ext.automap import automap_base


def get_all():
    Base = automap_base()
    Base.prepare(autoload_with=db.engine)
    Patients = Base.classes.PATIENTS
    Pharmacies = Base.classes.PHARMACIES
    Transactions = Base.classes.TRANSACTIONS

    join_query = db.session.query(Patients.UUID.label('PATIENT_UUID'), Patients.FIRST_NAME, Patients.LAST_NAME, Patients.DATE_OF_BIRTH, Pharmacies.UUID.label('PHARMACY_UUID'), Pharmacies.NAME, Pharmacies.CITY, Transactions.UUID.label('TRANSACTION_UUID'), Transactions.AMOUNT,
                                  Transactions.TIMESTAMP).join(Pharmacies).join(Patients)

    results = join_query.all()

    return jsonify([r._asdict() for r in results])
