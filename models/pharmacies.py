from database.services.service import db
from flask import jsonify
from sqlalchemy import func
from sqlalchemy.ext.automap import automap_base


def get_all():
    pharmacies = db.Table('PHARMACIES', db.metadata, autoload_with=db.engine)
    results = db.session.query(pharmacies).all()

    return jsonify([r._asdict() for r in results])


def get_user():
    Base = automap_base()
    Base.prepare(autoload_with=db.engine)
    pharmacies = Base.classes.PHARMACIES

    results = db.session.query(func.row_number().over(
        order_by=pharmacies.UUID.desc())).first()

    return results._asdict()
