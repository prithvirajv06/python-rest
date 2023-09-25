from flask import request, make_response
from flask_restful import Resource
from selenium import webdriver

from app.driver.web_driver_services import OneMoreExecutor as oe, OneMoreExecutor
from app.test_case.testcase_models import TestCase, TestCaseSchema
from app.utils.session_validation import is_valid_user
from server import db


class OneMoreWebDriver(Resource):
    @staticmethod
    def post() -> Resource:
        input_data = request.get_json()
        input_data, status, user = is_valid_user(input_data)
        if (status == 401):
            return make_response(input_data, status)
        else:
            response, status = oe.open_application(OneMoreExecutor,test_suite=input_data)
            return make_response(response, status)
