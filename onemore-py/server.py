"""App entry point."""

"""Initialize Flask app."""
import os
from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_cors import CORS

db = SQLAlchemy()
mail = Mail()


def create_app():
    """Construct the core application."""
    app_flask = Flask(__name__, instance_relative_config=False)
    mail = Mail(app_flask)

    # This is the configuration for the email server.
    app_flask.config["MAIL_SERVER"] = "smtp.gmail.com"
    app_flask.config["MAIL_PORT"] = 465
    app_flask.config["MAIL_USERNAME"] = os.environ.get("EMAIL_HOST_USER")
    app_flask.config["MAIL_PASSWORD"] = os.environ.get("EMAIL_HOST_PASSWORD")
    app_flask.config["MAIL_USE_TLS"] = False
    app_flask.config["MAIL_USE_SSL"] = True

    mail = Mail(app_flask)

    app_flask.config.from_object("config.Config")


    api = Api(app=app_flask)
    from app.workspace.workspace_routes import create_workspace_routes
    from app.test_suite.testsuite_routes import create_testsuite_routes
    from app.test_case.testcase_routes import create_testcase_routes
    from app.users.user_routes import create_authentication_routes

    create_authentication_routes(api=api)
    create_workspace_routes(api=api)
    create_testsuite_routes(api=api)
    create_testcase_routes(api=api)

    db.init_app(app_flask)

    with app_flask.app_context():
        db.create_all()  # Create database tables for our data models

        return app_flask


if __name__ == "__main__":
    app = create_app()
    CORS(app,allow_headers=['Authorization'])
    app.run(host="0.0.0.0", port=5000)
