import json

from marshmallow import EXCLUDE

from app.test_case_block.testcase_block_models import TestCaseBlock, TestCaseBlockSchema
from app.test_case_block.testcase_block_validation import Create_TCB_Save_Schema
from app.utils.common import generate_response
from app.utils.http_code import HTTP_201_CREATED, HTTP_200_OK, HTTP_204_NO_CONTENT
from server import db


def create_test_case_block(request, input_data, user):
    create_validation_schema = Create_TCB_Save_Schema(unknown=EXCLUDE)
    errors = create_validation_schema.validate(input_data)
    if (errors):
        return generate_response(message=errors)
    input_data['user'] = user
    new_test_case = TestCaseBlock(**input_data)
    db.session.add(new_test_case)
    db.session.commit()
    return generate_response(
        data=input_data, message="Test Suite Created", status=HTTP_201_CREATED
    )


def get_all_test_case_block(test_suite):
    result = db.session.query(TestCaseBlock.id, TestCaseBlock.test_case_type, TestCaseBlock.test_suite, TestCaseBlock.testcase_name,
                              TestCaseBlock.user).filter(
        TestCaseBlock.test_suite == test_suite).all()
    db.session.close()
    schema = TestCaseBlockSchema(many=True)
    return generate_response(
        data=schema.dump(result), message="Fetched all Test Suite", status=HTTP_200_OK)


def get_test_case_block(test_suite, test_case):
    result = db.session.query(TestCaseBlock).filter(TestCaseBlock.test_suite == test_suite, TestCaseBlock.id == test_case).one()
    db.session.close()
    schema = TestCaseBlockSchema(many=False)
    return generate_response(
        data=schema.dump(result), message="Fetched all Test Suite", status=HTTP_200_OK)


def delete_test_case_block(input_data):
    result = db.session.query(TestCaseBlock).filter(TestCaseBlock.id == input_data['id']).delete()
    if (result == 0):
        return generate_response(
            data={}, message="Test Suite not found", status=HTTP_204_NO_CONTENT)
    db.session.commit()
    schema = TestCaseBlockSchema(many=True)
    return generate_response(
        data={}, message="Test Suite Deleted from workspace", status=HTTP_200_OK)


def update_testcase(input_data, user):
    input_data['user'] = user
    db.session.query(TestCaseBlock).filter(TestCaseBlock.user == user, TestCaseBlock.id == input_data['id']).update(input_data)
    db.session.commit()
    db.session.close()
    return generate_response(
        data=input_data, message="Testcase Updated", status=HTTP_201_CREATED
    )
