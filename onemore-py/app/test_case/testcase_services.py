import json

from app.test_case.testcase_models import TestCase, TestCaseSchema
from app.test_case.testcase_validation import Create_TC_Save_Schema
from app.utils.common import generate_response
from app.utils.http_code import HTTP_201_CREATED, HTTP_200_OK, HTTP_204_NO_CONTENT
from server import db


def create_test_case(request, input_data, user):
    create_validation_schema = Create_TC_Save_Schema()
    errors = create_validation_schema.validate(input_data)
    if (errors):
        return generate_response(message=errors)
    input_data['user'] = user
    new_test_case = TestCase(**input_data)
    db.session.add(new_test_case)
    db.session.commit()
    return generate_response(
        data=input_data, message="Test Suite Created", status=HTTP_201_CREATED
    )


def get_all_test_case(workspace):
    result = db.session.query(TestCase).filter(TestCase.workspace == workspace).all()
    schema = TestCase(many=True)
    return generate_response(
        data=schema.dump(result), message="Fetched all Test Suite", status=HTTP_200_OK)

def delete_test_case(input_data):
    result = db.session.query(TestCase).filter(TestCase.id == input_data['id']).delete()
    if(result==0):
        return generate_response(
            data={}, message="Test Suite not found", status=HTTP_204_NO_CONTENT)
    db.session.commit()
    schema = TestCaseSchema(many=True)
    return generate_response(
        data={}, message="Test Suite Deleted from workspace", status=HTTP_200_OK)
