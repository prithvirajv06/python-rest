from flask_restful import Api

from app.test_case.testcase_view import DeleteTestCase, GetAllTestCase, CreateTestCase, UpdateTestCase, GetTestCase


def create_testcase_routes(api: Api):
    api.add_resource(CreateTestCase, "/api/test-case/save/")
    api.add_resource(UpdateTestCase, "/api/test-case/update/")
    api.add_resource(GetAllTestCase, "/api/test-case/get-ts-tc/")
    api.add_resource(GetTestCase, "/api/test-case/get-test-case/")
    api.add_resource(DeleteTestCase, "/api/test-case/delete-ts-tc/")
