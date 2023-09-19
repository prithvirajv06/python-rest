from flask_restful import Api

from app.test_suite.testsuite_view import CreateTestSuite, GetAllTestSuite, DeleteTestSuite


def create_testsuite_routes(api: Api):
    api.add_resource(CreateTestSuite, "/api/test-suite/save/")
    api.add_resource(GetAllTestSuite, "/api/test-suite/get-ws-ts/")
    api.add_resource(DeleteTestSuite, "/api/test-suite/delete-ws-ts/")
