from flask import request
from flask.views import MethodView
from flask_jwt_extended import get_jwt, jwt_required
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import IntegrityError, SQLAlchemyError

from db import db
from models import DogModel
from schemas import DogSchema

blp = Blueprint("dogs", __name__, description="Operations on dogs")


@blp.route("/api/dog")
class DogList(MethodView):
    @blp.response(200, DogSchema(many=True))
    def get(self):
        return DogModel.query.all()

    @jwt_required()
    @blp.arguments(DogSchema)
    @blp.response(201, DogSchema)
    def post(self, dog_data):
        dog = DogModel(**dog_data)

        try:
            db.session.add(dog)
            db.session.commit()
        except IntegrityError:
            abort(400, message="A dog with that name already exists.")
        except SQLAlchemyError:
            abort(500, message="An error ocurred while inserting the dog")

        return dog_data


@blp.route("/api/dog/<int:id>")
class Dog(MethodView):
    @blp.response(200, DogSchema)
    def get(self, id):
        dog = DogModel.query.get_or_404(id)
        return dog

    @jwt_required()
    def delete(self, id):
        jwt = get_jwt()
        if not jwt.get("is_admin"):
            abort(401, message="Admin privilege required.")

        dog = DogModel.query.get_or_404(id)
        db.session.delete(dog)
        db.session.commit()

        return {"message": "Dog entry deleted."}
