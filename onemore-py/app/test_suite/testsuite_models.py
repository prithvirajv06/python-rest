from dataclasses import dataclass

from marshmallow import Schema, fields

from server import db


@dataclass
class TestSuite(db.Model):
    __tablename__ = "test_suite"
    id = db.Column(db.Integer, primary_key=True)
    testsuite_name = db.Column(db.String(150), nullable=False)
    description = db.Column(db.String(500), nullable=True)
    user = db.Column(db.String(10), db.ForeignKey("users.id"), nullable=False)
    workspace = db.Column(db.String(10), db.ForeignKey("workspace.id"), nullable=False)
    application = db.Column()
    loaderCss = db.Column()

    def __init__(self, **kwargs):
        """
        The function takes in a dictionary of keyword arguments and assigns the values to the class
        attributes
        """
        self.testsuite_name = kwargs.get("testsuite_name")
        self.description = kwargs.get("description")
        self.user = kwargs.get("user")
        self.workspace = kwargs.get("workspace")
        self.application = kwargs.get("application")
        self.loaderCss = kwargs.get("loaderCss")

    def __repr__(self):
        """
        The __repr__ function is used to return a string representation of the object
        :return: The username of the user.
        """
        return "<Testsuite {}>".format(self.testsuite_name)


class TestsuiteSchema(Schema):
    id = fields.Str()
    testsuite_name = fields.Str()
    description = fields.Str()
    user = fields.Str()
    application = fields.Str()
    loaderCss = fields.Str()
