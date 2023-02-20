from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import IntegrityError, SQLAlchemyError

from db import db
from models import VaccineModel
from schemas import VaccineSchema

blp = Blueprint("vaccines", __name__, description="Operations on vaccines")


@blp.route("/api/vaccine")
class VaccineList(MethodView):
    @blp.response(200, VaccineSchema(many=True))
    def get(self):
        return VaccineModel.query.all()

    @blp.arguments(VaccineSchema)
    @blp.response(201, VaccineSchema)
    def post(self, vaccine_data):
        vaccine = VaccineModel(**vaccine_data)

        try:
            db.session.add(vaccine)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error ocurred while inserting the vaccine")

        return vaccine_data


@blp.route("/api/vaccine/<int:id>")
class Vaccine(MethodView):
    @blp.response(200, VaccineSchema)
    def get(self, id):
        vaccine = VaccineModel.query.get_or_404(id)
        return vaccine

    def delete(self, id):
        vaccine = VaccineModel.query.get_or_404(id)
        db.session.delete(vaccine)
        db.session.commit()

        return {"message": "Vaccine entry deleted."}
