import flask
import jwt

from app.users.user_models import User
from app.utils.common import TokenGenerator, generate_response
from app.utils.http_code import HTTP_401_UNAUTHORIZED


def is_valid_user(input_data):
    headers = flask.request.headers
    bearer = headers.get('Authorization')  # Bearer YourTokenHere
    if bearer is None:
        return generate_response(
            message="Token not provided.",
            status=HTTP_401_UNAUTHORIZED,
        )[0], HTTP_401_UNAUTHORIZED, None
    token = bearer.split()[1]  # YourTokenHere
    if token is None:
        return generate_response(
            message="Token is not valid.",
            status=HTTP_401_UNAUTHORIZED,
        )[0], HTTP_401_UNAUTHORIZED, None
    try:
        token = TokenGenerator.decode_token(token)
    except jwt.InvalidSignatureError:
        return generate_response(
            message="Token unauthorized.",
            status=HTTP_401_UNAUTHORIZED,
        )[0], HTTP_401_UNAUTHORIZED, None
    except jwt.ExpiredSignatureError:
        return generate_response(
            message="Token unauthorized.",
            status=HTTP_401_UNAUTHORIZED,
        )[0], HTTP_401_UNAUTHORIZED, None
    user = User.query.filter_by(id=token.get('id')).first()
    if user is None:
        return generate_response(
            message="Token unauthorized, User not found for the token provided.",
            status=HTTP_401_UNAUTHORIZED,
        )[0], HTTP_401_UNAUTHORIZED, None
    user_id = token.get('id')
    return input_data, True, user_id
