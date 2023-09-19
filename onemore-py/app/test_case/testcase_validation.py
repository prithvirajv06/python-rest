from marshmallow import fields, Schema, validate


class Create_TC_Save_Schema(Schema):
    testcase_name = fields.Str(required=True, validate=validate.Length(min=4))
    description = fields.Str(required=True, validate=validate.Length(min=4))
    test_suite =  fields.Str(required=True, validate=validate.Length(min=4))