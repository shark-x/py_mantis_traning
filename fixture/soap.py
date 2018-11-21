
from suds.client import  Client
from suds import WebFault
from model.project import Project

class SoapHelper:

    def __init__(self, app):
        self.app = app

    def can_login(self, username, password):
        client = Client("http://localhost/mantisbt-1.2.20/api/soap/mantisconnect.php?wsdl")
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def convert_projects_to_model(self, projects):
        def convert(project):
            return Project(project_name=project.name, id=str(project.id))
        return list(map(convert, projects))

    # def get_project_list(self, username, password):
    #     client = Client("http://localhost/mantisbt-1.2.20/api/soap/mantisconnect.php?wsdl")
    #     try:
    #         project_list = client.service.mc_projects_get_user_accessible(username, password)
    #         return self.convert_projects_to_model(project_list)
    #     except WebFault:
    #         return False

    def get_project_list(self):
        client = Client("http://localhost/mantisbt-1.2.20/api/soap/mantisconnect.php?wsdl")
        try:
            project_list = client.service.mc_projects_get_user_accessible(
                self.app.config['webadmin']['username'], self.app.config['webadmin']['password'])
            return self.convert_projects_to_model(project_list)
        except WebFault:
            return False