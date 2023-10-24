from flask import request, make_response
from flask_restful import Resource

from app.test_case.testcase_services import get_all_test_case, delete_test_case, create_test_case, update_testcase, \
    get_test_case
from app.utils.session_validation import is_valid_user


class CreateTestCaseBlock(Resource):
    @staticmethod
    def post() -> Resource:
        input_data = request.get_json()
        input_data, status, user = is_valid_user(input_data)
        if (status == 401):
            return make_response(input_data, status)
        else:
            response, status = create_test_case(request, input_data, user)
            return make_response(response, status)


class GetAllTestCaseBlock(Resource):
    @staticmethod
    def post() -> Resource:
        input_data = request.get_json()
        input_data, status, user = is_valid_user(input_data=input_data)
        if (status == 401):
            return make_response(input_data, status)
        else:
            response, status = get_all_test_case(input_data['testsuite'])
            return make_response(response, status)


class GetTestCaseBlock(Resource):
    @staticmethod
    def post() -> Resource:
        input_data = request.get_json()
        input_data, status, user = is_valid_user(input_data=input_data)
        if (status == 401):
            return make_response(input_data, status)
        else:
            response, status = get_test_case(input_data['test_suite'], input_data['id'])
            return make_response(response, status)


class DeleteTestCaseBlock(Resource):
    @staticmethod
    def post() -> Resource:
        input_data = request.get_json()
        input_data, status, user = is_valid_user(input_data=input_data)
        if (status == 401):
            return make_response(input_data, status)
        else:
            response, status = delete_test_case(input_data)
            return make_response(response, status)


class UpdateTestCaseBlock(Resource):
    @staticmethod
    def post() -> Resource:
        input_data, status, user = is_valid_user(request.get_json())
        if (status == 401):
            return make_response(input_data, status)
        else:
            response, status = update_testcase(input_data, user)
            return make_response(response, status)
