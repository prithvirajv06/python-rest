from flask_restful import Api

from app.workspace.wspace_view import CreateWorkSpace


def create_workspace_routes(api:Api):
    api.add_resource(CreateWorkSpace,"/api/workspace/save/")