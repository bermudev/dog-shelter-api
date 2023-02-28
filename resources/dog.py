from flask import request
from flask.views import MethodView
from flask_jwt_extended import get_jwt, jwt_required
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import IntegrityError, SQLAlchemyError

from db import db
from models import DogModel
from schemas import DogSchema, DogUpdateSchema

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

    @jwt_required(fresh=True)
    def delete(self, id):
        jwt = get_jwt()
        if not jwt.get("is_admin"):
            abort(401, message="Admin privilege required.")

        dog = DogModel.query.get_or_404(id)
        db.session.delete(dog)
        db.session.commit()

        return {"message": "Dog entry deleted."}

    @jwt_required()
    @blp.arguments(DogUpdateSchema)
    @blp.response(200, DogSchema)
    def put(self, dog_data, id):
        dog = DogModel.query.get(id)
        if dog:
            dog.name = dog_data["name"]
            dog.breed = dog_data["breed"]
            dog.age = dog_data["age"]
            dog.gender = dog_data["gender"]
            dog.size = dog_data["size"]
            dog.description = dog_data["description"]
            dog.picture_url = dog_data["picture_url"]
            dog.adopted = dog_data["adopted"]
        else:
            dog = DogModel(id=id, **dog_data)

        db.session.add(dog)
        db.session.commit()

        return dog
