from flask_restful import Api

from app.workspace.wspace_view import CreateWorkSpace, GetAllMyWorkspace, GetALlRecordsCount, UpdateWorkspace, \
    GetWorkspace


def create_workspace_routes(api: Api):
    api.add_resource(CreateWorkSpace, "/api/workspace/save/")
    api.add_resource(GetALlRecordsCount, "/api/workspace/get-ws-count/")
    api.add_resource(GetAllMyWorkspace, "/api/workspace/get-all-my-ws/")
    api.add_resource(UpdateWorkspace, "/api/workspace/update-ws/")
    api.add_resource(GetWorkspace, "/api/workspace/get-ws/")
