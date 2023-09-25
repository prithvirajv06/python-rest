from flask_restful import Api

from app.driver.web_driver_view import OneMoreWebDriver


def create_driver_routes(api: Api):
    api.add_resource(OneMoreWebDriver, "/api/test-driver/execute-ts")
