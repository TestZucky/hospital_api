from marshmallow import Schema, fields, validate

class DoctorSchema(Schema):
    doctor_id = fields.Int(dump_only=True)
    doctor_name = fields.Str(required=True, validate=validate.Length(min=1))
    doctor_email = fields.Email(required=True, validate=validate.Length(min=1))
    doctor_password = fields.Str(required=True, validate=validate.Length(min=6))
    doctor_active = fields.Bool(required=True)
    store_id = fields.Int(required=True)
    user_role = fields.Str(required=True)