from marshmallow import fields, Schema, validate


class Create_WS_SaveSchema(Schema):
    workspace_name = fields.Str(required=True, validate=validate.Length(min=4))
    description = fields.Str(required=True, validate=validate.Length(min=4))