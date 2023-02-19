from marshmallow import Schema, fields


class DogSchema(Schema):
    # id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    breed = fields.Str(required=True)
    age = fields.Int(required=True)
    gender = fields.Str(required=True)
    size = fields.Str(required=True)
    description = fields.Str(required=True)
    picture_url = fields.Str(required=True)
    adopted = fields.Bool(required=True)


class VaccineSchema(Schema):
    # id = fields.Int(dump_only=True)
    dog_id = fields.Int(required=True)
    vaccine_name = fields.Str(required=True)
    vaccine_date = fields.DateTime(dt_format="iso8601", required=True)
