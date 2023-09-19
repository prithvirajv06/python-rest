from marshmallow import fields, Schema, validate


class Create_TS_Save_Schema(Schema):
    testsuite_name = fields.Str(required=True, validate=validate.Length(min=4))
    description = fields.Str(required=True, validate=validate.Length(min=4))
    workspace =  fields.Str(required=True, validate=validate.Length(min=4))