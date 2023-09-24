from selenium import webdriver

from app.test_case.testcase_models import TestCase, TestCaseSchema
from server import db


class OneMoreWebDriver():
    browser = webdriver.Chrome()

    def execute_test_suite(self, testsuite_id):
        get_all_test_case(test_suite=testsuite_id)


def get_all_test_case(test_suite):
    result = db.session.query(TestCase).filter(
        TestCase.test_suite == test_suite).all()
    db.session.close()
    schema = TestCaseSchema(many=True)
    return schema
