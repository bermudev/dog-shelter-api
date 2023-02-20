from db import db


class VaccineModel(db.Model):
    __tablename__ = "vaccines"

    id = db.Column(db.Integer, primary_key=True)
    vaccine_name = db.Column(db.String(80), unique=False, nullable=False)
    vaccine_date = db.Column(db.String, unique=False, nullable=False)

    dog_id = db.Column(
        db.Integer, db.ForeignKey("dogs.id"), unique=False, nullable=False
    )
    dog = db.relationship("DogModel", back_populates="vaccines")
