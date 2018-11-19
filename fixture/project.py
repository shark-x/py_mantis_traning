from model.project import Project
import random
import string

class ProjectHelper:

    def __init__(self, app):
        self. app = app

    def open_project_page(self):
        wd = self.app.wd
        if not wd.current_url.endswith("/manage_proj_page.php"):
            wd.find_element_by_link_text("Manage").click()
            wd.find_element_by_link_text("Manage Projects").click()

    def create(self, project):
        wd = self.app.wd
        self.open_project_page()
        wd.find_element_by_xpath("//input[@value='Create New Project']").click()
        self.fill_form(project)
        wd.find_element_by_xpath("//input[@value='Add Project']").click()
        wd.find_element_by_link_text("Proceed").click()
        self.app.open_home_page()
        self.project_cache = None

    def fill_form(self, project):
        wd = self.app.wd
        self.change_field_project("name", project.project_name)
        # self.change_field_project("status", project.status)
        # self.change_field_project("inherit_global", project.inherit_gl_cat)
        # self.change_field_project("view_state", project.view_status)
        # self.change_field_project("description", project.description)

    def change_field_project(self, field, text):
        wd = self.app.wd
        wd.find_element_by_name(field).click()
        wd.find_element_by_name(field).clear()
        wd.find_element_by_name(field).send_keys(text)

    # def there_is_no_projects(self):
    #     wd = self.app.wd
    #     project_table = self.select_project_table()
    #     return project_table.find_element_by_xpath("//tr[@class='row-1']") == 0

    def select_project_table(self):
        wd = self.app.wd
        self.open_project_page()
        return wd.find_element_by_xpath("//table[@class='width100'][@cellspacing='1']")

    def project_that_name_exists(self, project_name):
        wd = self.app.wd
        project_list = self.get_project_list()
        for element in project_list:
            if element.project_name == project_name:
                return True

    project_cache = None

    def get_project_list(self):
        if self.project_cache is None:
            wd = self.app.wd
            self.open_project_page()
            self.project_cache = []
            project_table = self.select_project_table()
            project_list = project_table.find_elements_by_tag_name("tr")
            for element in project_list[2:]:
                project_name = element.find_element_by_tag_name("a").text
                st = element.find_element_by_tag_name("a").get_attribute("href")
                from_x = st.find('id=') + 3
                id = st[from_x:]
                self.project_cache.append(Project(project_name=project_name, id=id))
        return list(self.project_cache)

    def generate_some_string(self):
        wd = self.app.wd
        length = random.randint(1, 9)
        symbols = string.ascii_letters + string.digits
        some_string = "".join([random.choice(symbols) for i in range(length)])
        return some_string

    def delete_by_name(self, project_name):
        wd = self.app.wd
        self.open_project_page()
        project_list = self.get_project_list()
        for element in project_list:
            if element.project_name == project_name:
                projects_table = self.select_project_table()
                projects_table.find_element_by_link_text("%s" % project_name).click()
                wd.find_element_by_xpath("//input[@value='Delete Project']").click()
                wd.find_element_by_xpath("//input[@value='Delete Project']").click()
            self.open_project_page()
            self.project_cache = None

    # def get_project_list(self):
    #     if self.project_cache is None:
    #         wd = self.app.wd
    #         self.open_project_page()
    #         self.project_cache = []