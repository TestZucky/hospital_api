from marshmallow import Schema, fields

class BlockListSchema(Schema):
    id = fields.Int(dump_only=True)
    jti = fields.Str(required=True)
    created_at = fields.DateTime(required=True)
