from dataclasses import dataclass

from marshmallow import Schema, fields

from server import db
from sqlalchemy.dialects.mysql import JSON


@dataclass
class TestCase(db.Model):
    __tablename__ = "test_case"
    id = db.Column(db.Integer, primary_key=True)
    testcase_name = db.Column(db.String(150), nullable=False)
    description = db.Column(db.String(500), nullable=True)
    user = db.Column(db.String(10), db.ForeignKey("users.id"), nullable=False)
    test_suite = db.Column(db.String(10), db.ForeignKey("test_suite.id"), nullable=False)
    test_case_type = db.Column(db.String(20))
    test_case_details = db.Column(JSON)

    def __init__(self, **kwargs):
        """
        The function takes in a dictionary of keyword arguments and assigns the values to the class
        attributes
        """
        self.testcase_name = kwargs.get("testcase_name")
        self.description = kwargs.get("description")
        self.user = kwargs.get("user")
        self.test_suite = kwargs.get("test_suite")
        self.test_case_type = kwargs.get("test_case_type")
        self.test_case_details = kwargs.get("test_Case_details")

    def __repr__(self):
        """
        The __repr__ function is used to return a string representation of the object
        :return: The username of the user.
        """
        return "<Testcase {}>".format(self.testcase_name)


class TestCaseSchema(Schema):
    id = fields.Str()
    testcase_name = fields.Str()
    description = fields.Str()
    user = fields.Str()
    test_suite = fields.Str()
    test_case_type = fields.Str()
    test_case_details = fields.Dict()


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
