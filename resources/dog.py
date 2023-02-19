from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort

from db import dogs
from schemas import DogSchema

blp = Blueprint("dogs", __name__, description="Operations on dogs")


@blp.route("/api/dog")
class DogList(MethodView):
    def get(self):
        return dogs

    @blp.arguments(DogSchema)
    def post(self, dog_data):
        for dog in dogs.values():
            if dog_data["name"] == dog["name"]:
                abort(400, message="Dog already exists.")

        key = max(dogs.keys()) + 1
        dogs[key] = dog_data
        return dog_data, 201


@blp.route("/api/dog/<int:id>")
class Dog(MethodView):
    def get(self, id):
        try:
            return dogs[id]
        except KeyError:
            abort(404, message="Dog not found.")

    def delete(self, id):
        try:
            del dogs[id]
            return {"message": "Dog deleted."}
        except KeyError:
            abort(404, message="Dog not found.")
