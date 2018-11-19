from model.project import Project
import random


def test_del_project(app):
    if len(app.project.get_project_list()) == 0:    # возвращает True если список проектов пустой
        project_name = app.project.generate_some_string()
        app.project.create(Project(project_name=project_name))
    old_project_list = app.project.get_project_list()
    project = random.choice(old_project_list)
    app.project.delete_by_name(project.project_name)
    new_project_list = app.project.get_project_list()
    old_project_list.remove(project)
    assert sorted(old_project_list, key=Project.id_or_max) == sorted(new_project_list, key=Project.id_or_max)
