from flask import request, make_response
from flask_restful import Resource

from app.utils.session_validation import is_valid_user
from app.test_suite.testsuite_services import create_test_suite, get_all_test_suite, delete_test_suite


class CreateTestSuite(Resource):
    @staticmethod
    def post() -> Resource:
        input_data = request.get_json()
        input_data, status, user = is_valid_user(input_data)
        if (status == 401):
            return make_response(input_data, status)
        else:
            response, status = create_test_suite(request, input_data, user)
            return make_response(response, status)


class GetAllTestSuite(Resource):
    @staticmethod
    def post() -> Resource:
        input_data = request.get_json()
        input_data, status, user = is_valid_user(input_data=input_data)
        if (status == 401):
            return make_response(input_data, status)
        else:
            response, status = get_all_test_suite(input_data['workspace'])
            return make_response(response, status)

class DeleteTestSuite(Resource):
    @staticmethod
    def post() -> Resource:
        input_data = request.get_json()
        input_data, status, user = is_valid_user(input_data=input_data)
        if (status == 401):
            return make_response(input_data, status)
        else:
            response, status = delete_test_suite(input_data)
            return make_response(response, status)
