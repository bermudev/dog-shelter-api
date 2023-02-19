from flask import Flask, request

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
        return {"message": "Dog not found"}, 404


@app.post("/api/dog")
def create_dog():
    dog_data = request.get_json()
    key = max(dogs.keys()) + 1
    dogs[key] = dog_data
    return dog_data, 201


@app.get("/api/vaccine")
def get_all_vaccines():
    return vaccines


@app.get("/api/vaccine/<int:id>")
def get_single_vaccine(id):
    try:
        return vaccines[id]
    except KeyError:
        return {"message": "Vaccine not found"}, 404


@app.post("/api/vaccine")
def create_vaccine():
    vaccine_data = request.get_json()
    key = max(vaccines.keys()) + 1
    vaccines[key] = vaccine_data
    return vaccine_data, 201
