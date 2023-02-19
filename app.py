from flask import Flask, request
from flask_smorest import abort

from db import dogs, vaccines

app = Flask(__name__)


@app.get("/api/dog")
def get_all_dogs():
    return dogs


@app.get("/api/dog/<int:id>")
def get_single_dog(id):
    try:
        return dogs[id]
    except KeyError:
        abort(404, message="Dog not found.")


@app.post("/api/dog")
def create_dog():
    dog_data = request.get_json()
    if (
        "name" not in dog_data
        or "breed" not in dog_data
        or "age" not in dog_data
        or "gender" not in dog_data
        or "size" not in dog_data
        or "picture_url" not in dog_data
        or "description" not in dog_data
        or "adopted" not in dog_data
    ):
        abort(400, message="Bad request. Ensure all the keys are present.")

    for dog in dogs.values():
        if dog_data["name"] == dog["name"]:
            abort(400, message="Dog already exists.")

    key = max(dogs.keys()) + 1
    dogs[key] = dog_data
    return dog_data, 201


@app.delete("/api/dog/<int:id>")
def delete_dog(id):
    try:
        del dogs[id]
        return {"message": "Dog deleted."}
    except KeyError:
        abort(404, message="Dog not found.")


@app.get("/api/vaccine")
def get_all_vaccines():
    return vaccines


@app.get("/api/vaccine/<int:id>")
def get_single_vaccine(id):
    try:
        return vaccines[id]
    except KeyError:
        abort(404, message="Vaccine not found.")


@app.post("/api/vaccine")
def create_vaccine():
    vaccine_data = request.get_json()
    if (
        "dog_id" not in vaccine_data
        or "vaccine_name" not in vaccine_data
        or "vaccine_date" not in vaccine_data
    ):
        abort(400, message="Bad request. Ensure all the keys are present.")

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


@app.delete("/api/vaccine/<int:id>")
def delete_vaccine(id):
    try:
        del vaccines[id]
        return {"message": "Vaccine deleted."}
    except KeyError:
        abort(404, message="Vaccine not found.")
