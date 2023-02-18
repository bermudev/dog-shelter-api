from flask import Flask, request
from db import dogs

app = Flask(__name__)


@app.get("/api/dogs")
def get_dogs():
    return {"dogs": list(dogs.values())}


@app.post("/api/dogs")
def create_dogs():
    dog_data = request.get_json()
    dog_id = len(dogs) + 1

    new_dog = {**dog_data, "id": dog_id}
    dogs[dog_id] = new_dog
    return new_dog, 201
