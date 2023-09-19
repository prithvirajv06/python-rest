import json

from app.utils.common import generate_response
from app.utils.http_code import HTTP_201_CREATED, HTTP_200_OK, HTTP_204_NO_CONTENT
from app.test_suite.testsuite_models import TestSuite, TestsuiteSchema
from app.test_suite.testsuite_validation import Create_TS_Save_Schema
from server import db
from app.workspace.wspace_models import Workspace, WorkspaceSchema


def create_test_suite(request, input_data, user):
    create_validation_schema = Create_TS_Save_Schema()
    errors = create_validation_schema.validate(input_data)
    if (errors):
        return generate_response(message=errors)
    input_data['user'] = user
    new_test_suite = TestSuite(**input_data)
    db.session.add(new_test_suite)
    db.session.commit()
    return generate_response(
        data=input_data, message="Test Suite Created", status=HTTP_201_CREATED
    )


def get_all_test_suite(workspace):
    result = db.session.query(TestSuite).filter(TestSuite.workspace == workspace).all()
    schema = TestSuite(many=True)
    return generate_response(
        data=schema.dump(result), message="Fetched all Test Suite", status=HTTP_200_OK)

def delete_test_suite(input_data):
    result = db.session.query(TestSuite).filter(TestSuite.id == input_data['id']).delete()
    if(result==0):
        return generate_response(
            data={}, message="Test Suite not found", status=HTTP_204_NO_CONTENT)
    db.session.commit()
    schema = TestsuiteSchema(many=True)
    return generate_response(
        data={}, message="Test Suite Deleted from workspace", status=HTTP_200_OK)
