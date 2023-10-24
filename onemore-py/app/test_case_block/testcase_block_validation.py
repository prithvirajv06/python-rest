from marshmallow import fields, Schema, validate


class Create_TCB_Save_Schema(Schema):
    testcase_block_name = fields.Str(required=True, validate=validate.Length(min=2))
    testcase_block_name_suite = fields.Str(required=True, validate=validate.Length(min=4))
