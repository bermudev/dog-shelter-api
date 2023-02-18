from flask import Flask, request

app = Flask(__name__)

dogs = [
    {
        "name": "Morvi",
        "breed": "Mix",
        "age": "3",
        "gender": "Male",
        "size": "Medium",
        "picture_url": "/morvi.jpg",
        "description": "Affectionate and loving doggy",
        "adopted": True,
    }
]


@app.get("/dogs")
def get_dogs():
    return {"dogs": dogs}


@app.post("/dogs")
def create_dogs():
    request_data = request.get_json()
    new_dog = {
        "name": request_data["name"],
        "breed": request_data["breed"],
        "age": request_data["age"],
        "gender": request_data["gender"],
        "size": request_data["size"],
        "picture_url": request_data["picture_url"],
        "description": request_data["description"],
        "adopted": request_data["adopted"],
    }
    dogs.append(new_dog)
    return new_dog, 201
