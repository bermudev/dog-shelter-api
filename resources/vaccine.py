from flask import request
from flask.views import MethodView
from flask_jwt_extended import get_jwt, jwt_required
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import IntegrityError, SQLAlchemyError

from db import db
from models import VaccineModel
from schemas import VaccineSchema, VaccineUpdateSchema

blp = Blueprint("vaccines", __name__, description="Operations on vaccines")


@blp.route("/api/vaccine")
class VaccineList(MethodView):
    @blp.response(200, VaccineSchema(many=True))
    def get(self):
        return VaccineModel.query.all()

    @jwt_required()
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

    @jwt_required(fresh=True)
    def delete(self, id):
        jwt = get_jwt()
        if not jwt.get("is_admin"):
            abort(401, message="Admin privilege required.")

        vaccine = VaccineModel.query.get_or_404(id)
        db.session.delete(vaccine)
        db.session.commit()

        return {"message": "Vaccine entry deleted."}

    @jwt_required()
    @blp.arguments(VaccineUpdateSchema)
    @blp.response(200, VaccineSchema)
    def put(self, vaccine_data, id):
        vaccine = VaccineModel.query.get(id)
        if vaccine:
            vaccine.vaccine_name = vaccine_data["vaccine_name"]
            vaccine.vaccine_date = vaccine_data["vaccine_date"]
        else:
            vaccine = VaccineModel(id=id, **vaccine_data)

        db.session.add(vaccine)
        db.session.commit()

        return vaccine
