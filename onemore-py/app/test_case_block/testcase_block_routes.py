from flask_restful import Api

from app.test_case_block.testcase_block_view import CreateTestCaseBlock, UpdateTestCaseBlock, GetAllTestCaseBlock, \
    GetTestCaseBlock, DeleteTestCaseBlock


def create_testcase_routes(api: Api):
    api.add_resource(CreateTestCaseBlock, "/api/test-case-block/save/")
    api.add_resource(UpdateTestCaseBlock, "/api/test-case-block/update/")
    api.add_resource(GetAllTestCaseBlock, "/api/test-case-block/get-ts-tc/")
    api.add_resource(GetTestCaseBlock, "/api/test-case-block/get-test-case/")
    api.add_resource(DeleteTestCaseBlock, "/api/test-case-block/delete-ts-tc/")
