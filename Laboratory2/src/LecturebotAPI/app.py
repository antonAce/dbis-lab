from flask import Flask, render_template, request, redirect, url_for

from LecturebotDAL.repository import Repository, UnitOfWork
from LecturebotDAL.models import Role, User, Lecture, UserHasResources, Resource, Component, Attribute
from LecturebotDAL.dbcontext import *

from LecturebotAPI.forms import RoleForm, LectureForm, ResourceForm

app = Flask(__name__)
app.secret_key = 'development key'


@app.route('/', methods=['GET'])
def index():
    return render_template('navigation.html')


@app.route('/role', methods=['GET', 'POST'])
def list_roles():
    repository = Repository.Repository(session, ModelBase, DBEngine)
    unit_of_work = UnitOfWork.UnitOfWork(session, ModelBase)
    roles = repository.get_all(Role.Role)
    form = RoleForm.RoleForm(request.form)

    if request.method == 'POST':
        print(form.id.data)

        new_role = Role.Role(name=form.Name.data, priority=form.Priority.data)
        repository.create(new_role)
        unit_of_work.commit()
        return redirect('/role')

    return render_template('role.html', roles=roles, form=form)


@app.route('/user', methods=['GET'])
def list_users():
    repository = Repository.Repository(session, ModelBase, DBEngine)
    users = repository.get_all(User.User)

    return render_template('user.html', users=users)


@app.route('/lecture', methods=['GET', 'POST'])
def list_lectures():
    repository = Repository.Repository(session, ModelBase, DBEngine)
    lectures = repository.get_all(Lecture.Lecture)

    return render_template('lecture.html', lectures=lectures)


@app.route('/userhasresources', methods=['GET'])
def list_resources_of_user():
    repository = Repository.Repository(session, ModelBase, DBEngine)
    resources_of_user = repository.get_all(UserHasResources.UserHasResources)

    return render_template('userhasresource.html', usersresources=resources_of_user)


@app.route('/resource', methods=['GET', 'POST'])
def list_resources():
    repository = Repository.Repository(session, ModelBase, DBEngine)
    resources = repository.get_all(Resource.Resource)

    return render_template('resource.html', resources=resources)


@app.route('/component', methods=['GET'])
def list_components():
    repository = Repository.Repository(session, ModelBase, DBEngine)
    components = repository.get_all(Component.Component)

    return render_template('component.html', components=components)


@app.route('/attribute', methods=['GET'])
def list_attributes():
    repository = Repository.Repository(session, ModelBase, DBEngine)
    attributes = repository.get_all(Attribute.Attribute)

    return render_template('attribute.html', attributes=attributes)


