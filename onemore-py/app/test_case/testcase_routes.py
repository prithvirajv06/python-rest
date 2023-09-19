from flask_restful import Api

from app.test_case.testcase_view import DeleteTestCase, GetAllTestCase, CreateTestCase


def create_testcase_routes(api: Api):
    api.add_resource(CreateTestCase, "/api/test-case/save/")
    api.add_resource(GetAllTestCase, "/api/test-case/get-ws-ts/")
    api.add_resource(DeleteTestCase, "/api/test-case/delete-ws-ts/")
