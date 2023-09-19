import json

from flask import jsonify
from marshmallow import Schema

from app.utils.common import generate_response, TokenGenerator
from app.utils.http_code import HTTP_201_CREATED, HTTP_401_UNAUTHORIZED, HTTP_200_OK
from app.workspace.wspace_validation import Create_WS_SaveSchema
from server import db
from app.workspace.wspace_models import Workspace, WorkspaceSchema
from sqlalchemy import select


def create_wspace(request, input_data, user):
    create_validation_schema = Create_WS_SaveSchema()
    errors = create_validation_schema.validate(input_data)
    if (errors):
        return generate_response(message=errors)
    input_data['user'] = user
    new_workspace = Workspace(**input_data)
    db.session.add(new_workspace)
    db.session.commit()
    return generate_response(
        data=input_data, message="Workspace Created", status=HTTP_201_CREATED
    )


def get_all_workspace(user):
    result = db.session.query(Workspace).filter(Workspace.user == user).all()
    schema = WorkspaceSchema(many=True)
    return generate_response(
        data=schema.dump(result), message="Fetched all workspace", status=HTTP_200_OK)
