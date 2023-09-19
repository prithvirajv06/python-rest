from flask_restful import Api

from app.workspace.wspace_view import CreateWorkSpace, GetAllMyWorkspace


def create_workspace_routes(api: Api):
    api.add_resource(CreateWorkSpace, "/api/workspace/save/")
    api.add_resource(GetAllMyWorkspace, "/api/workspace/get-all-my-ws/")
