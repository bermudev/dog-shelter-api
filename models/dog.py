from db import db


class DogModel(db.Model):
    __tablename__ = "dogs"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    breed = db.Column(db.String(80), unique=False, nullable=False)
    age = db.Column(db.Integer, unique=False, nullable=False)
    gender = db.Column(db.String(10), unique=False, nullable=False)
    size = db.Column(db.String(10), unique=False, nullable=False)
    picture_url = db.Column(db.String(80), unique=False, nullable=False)
    description = db.Column(db.String(100), unique=False, nullable=False)
    adopted = db.Column(db.Boolean, unique=False, nullable=False)

    vaccines = db.relationship(
        "VaccineModel", back_populates="dog", lazy="dynamic", cascade="all, delete"
    )
