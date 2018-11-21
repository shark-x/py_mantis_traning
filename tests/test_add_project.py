from model.project import Project


def test_add_project(app):
    # project_name = "project1"
    project_name = app.project.generate_some_string()
    # old_project_list = app.project.get_project_list()
    old_project_list = app.soap.get_project_list()
    project = Project(project_name=project_name)
    if len(old_project_list) == 0:    # возвращает True если список проектов пустой
         app.project.create(project)
    else:
        if app.project.project_that_name_exists(project_name):  # возвращает True, если уже есть проект с таким именем
            some_string = app.project.generate_some_string()
            app.project.create(Project(project_name=some_string))
        else:
            app.project.create(project)
    # new_project_list = app.project.get_project_list()
    new_project_list = app.soap.get_project_list()
    old_project_list.append(project)
    assert sorted(old_project_list, key=Project.id_or_max) == sorted(new_project_list, key=Project.id_or_max)
