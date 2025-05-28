from marshmallow import Schema, fields

class UserSchema(Schema):
    user_id = fields.Int(dump_only=True)
    user_name = fields.Str(required=True)
    user_password = fields.Str(required=True, load_only=True)
    user_city = fields.Str(required=True)
    user_state = fields.Str(required=True)
    user_role = fields.Str(required=True)
    user_email = fields.Str(required=True)
