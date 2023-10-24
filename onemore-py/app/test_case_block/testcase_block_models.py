from dataclasses import dataclass

from marshmallow import Schema, fields

from server import db
from sqlalchemy.dialects.mysql import JSON


@dataclass
class TestCaseBlock(db.Model):
    __tablename__ = "test_case"
    id = db.Column(db.Integer, primary_key=True)
    testcase_block_name = db.Column(db.String(150), nullable=False)
    description = db.Column(db.String(500), nullable=True)
    user = db.Column(db.String(10), db.ForeignKey("users.id"), nullable=False)
    test_suite = db.Column(db.String(10), db.ForeignKey("test_suite.id"), nullable=False)

    def __init__(self, **kwargs):
        """
        The function takes in a dictionary of keyword arguments and assigns the values to the class
        attributes
        """
        self.testcase_block_name = kwargs.get("testcase_block_name")
        self.description = kwargs.get("description")
        self.user = kwargs.get("user")
        self.test_suite = kwargs.get("test_suite")

    def __repr__(self):
        """
        The __repr__ function is used to return a string representation of the object
        :return: The username of the user.
        """
        return "<Testcase {}>".format(self.testcase_block_name)


class TestCaseBlockSchema(Schema):
    id = fields.Str()
    testcase_block_name = fields.Str()
    description = fields.Str()
    user = fields.Str()
    test_suite = fields.Str()


import json
from marshmallow import fields


class JSON(fields.Field):
    def _deserialize(self, value, attr, data, **kwargs):
        if value:
            try:
                return json.loads(value)
            except ValueError:
                return None

        return None
