from marshmallow import Schema, fields, validate

class StoreSchema(Schema):
    store_id = fields.Int(dump_only=True)
    store_name = fields.Str(required=True, validate=validate.Length(min=1))
    store_landmark = fields.Str(required=True, validate=validate.Length(min=1))
    store_city = fields.Str(required=True, validate=validate.Length(min=1))
    store_state = fields.Str(required=True, validate=validate.Length(min=1))
    store_owner = fields.Str(required=True, validate=validate.Length(min=1))
    store_zip_code = fields.Str(required=True, validate=lambda z: len(z) == 6)
    store_active = fields.Bool(required=True)
