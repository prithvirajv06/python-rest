import json

from flask import jsonify
from flask_sqlalchemy import BaseQuery
from marshmallow import Schema

from app.utils.common import generate_response, TokenGenerator
from app.utils.http_code import HTTP_201_CREATED, HTTP_401_UNAUTHORIZED, HTTP_200_OK
from app.workspace.wspace_validation import Create_WS_SaveSchema, Create_WS_UpdateSchema
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
    db.session.close()
    return generate_response(
        data=input_data, message="Workspace Created", status=HTTP_201_CREATED
    )


def update_wspace(request, input_data, user):
    create_validation_schema = Create_WS_UpdateSchema()
    errors = create_validation_schema.validate(input_data)
    if (errors):
        return generate_response(message=errors)
    input_data['user'] = user
    db.session.query(Workspace).filter(Workspace.user == user, Workspace.id == input_data['id']).update(input_data)
    db.session.commit()
    db.session.close()
    return generate_response(
        data=input_data, message="Workspace Updated", status=HTTP_201_CREATED
    )


def get_all_workspace(user, per_page, page):
    query = db.session.query(Workspace).filter(Workspace.user == user).paginate(page=page, per_page=per_page)
    db.session.close()
    result = query.items
    schema = WorkspaceSchema(many=True)
    return generate_response(
        data=schema.dump(result), message="Fetched all workspace", status=HTTP_200_OK)


def get_total_record(user):
    query = db.session.query(Workspace).filter(Workspace.user == user).count()
    db.session.close()
    return generate_response(
        data={'count': query}, message="Fetched all workspace", status=HTTP_200_OK)


def paginate(sa_query, page, per_page=20, error_out=True):
    sa_query.__class__ = BaseQuery
    # We can now use BaseQuery methods like .paginate on our SA query
    return sa_query.paginate(page, per_page, error_out)


def get_wspace(wspace_id):
    query_res = db.session.query(Workspace).filter(Workspace.id == wspace_id).one()
    db.session.close()
    schema = WorkspaceSchema(many=False)
    return generate_response(
        data=schema.dump(query_res), message="Fetched all workspace", status=HTTP_200_OK)
