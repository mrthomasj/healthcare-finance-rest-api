from database.services.service import db
from flask import jsonify


def get_all():
    patients = db.Table('PATIENTS', db.metadata, autoload_with=db.engine)
    results = db.session.query(patients).all()

    return jsonify([r._asdict() for r in results])
