from app.utils.common import generate_response, TokenGenerator
from app.utils.http_code import HTTP_201_CREATED, HTTP_401_UNAUTHORIZED
from app.workspace.wspace_validation import Create_WS_SaveSchema
from server import db
from app.workspace.wspace_models import Workspace


def create_wspace(request, input_data, user):
    create_validation_schema = Create_WS_SaveSchema()
    errors = create_validation_schema.validate(input_data)
    if (errors):
        return generate_response(message=errors)
    input_data['user'] = user
    new_workspace = Workspace(**input_data)
    db.session.add(new_workspace)
    db.session.commit()
    return generate_response(
        data=input_data, message="Workspace Created", status=HTTP_201_CREATED
    )
