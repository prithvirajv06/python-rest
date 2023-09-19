import flask
from flask import request, make_response
from flask_restful import Resource

from app.utils.session_validation import is_valid_user
from app.workspace.wspace_services import create_wspace, get_all_workspace


class CreateWorkSpace(Resource):
    @staticmethod
    def post() -> Resource:
        input_data = request.get_json()
        input_data, status, user = is_valid_user(input_data)
        if (status == 401):
            return make_response(input_data, status)
        else:
            response, status = create_wspace(request, input_data, user)
            return make_response(response, status)


class GetAllMyWorkspace(Resource):
    @staticmethod
    def post() -> Resource:
        input_data, status, user = is_valid_user(None)
        if (status == 401):
            return make_response(input_data, status)
        else:
            response, status = get_all_workspace(user)
            return make_response(response, status)
