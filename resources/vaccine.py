from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort

from db import dogs, vaccines
from schemas import VaccineSchema

blp = Blueprint("vaccines", __name__, description="Operations on vaccines")


@blp.route("/api/vaccine")
class VaccineList(MethodView):
    def get(self):
        return vaccines

    @blp.arguments(VaccineSchema)
    def post(self, vaccine_data):
        for vaccine in vaccines.values():
            if (
                vaccine_data["dog_id"] == vaccine["dog_id"]
                and vaccine_data["vaccine_name"] == vaccine["vaccine_name"]
            ):
                abort(400, message="Vaccine already exists for that dog.")

        if vaccine_data["dog_id"] not in dogs:
            abort(400, message="Dog not found.")

        key = max(vaccines.keys()) + 1
        vaccines[key] = vaccine_data
        return vaccine_data, 201


@blp.route("/api/vaccine/<int:id>")
class Vaccine(MethodView):
    def get(self, id):
        try:
            return vaccines[id]
        except KeyError:
            abort(404, message="Vaccine not found.")

    def delete(self, id):
        try:
            del vaccines[id]
            return {"message": "Vaccine deleted."}
        except KeyError:
            abort(404, message="Vaccine not found.")
