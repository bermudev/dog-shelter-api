from marshmallow import Schema, fields


class PlainDogSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    breed = fields.Str(required=True)
    age = fields.Int(required=True)
    gender = fields.Str(required=True)
    size = fields.Str(required=True)
    description = fields.Str(required=True)
    picture_url = fields.Str(required=True)
    adopted = fields.Bool(required=True)


class PlainVaccineSchema(Schema):
    id = fields.Int(dump_only=True)
    vaccine_name = fields.Str(required=True)
    vaccine_date = fields.Str(required=True)


class VaccineSchema(PlainVaccineSchema):
    dog_id = fields.Int(required=True, load_only=True)
    dog = fields.Nested(PlainDogSchema(), dump_only=True)


class DogSchema(PlainDogSchema):
    vaccines = fields.List(fields.Nested(PlainVaccineSchema()), dump_only=True)


class VaccineUpdateSchema(Schema):
    vaccine_name = fields.Str()
    vaccine_date = fields.Str()
    dog_id = fields.Int()


class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True)
    password = fields.Str(required=True, load_only=True)
