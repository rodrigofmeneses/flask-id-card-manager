from flask import Blueprint, flash, jsonify, render_template, redirect, request, url_for
from app.ext.wtforms.forms import EmployeeForm
from app.models import Employee
from app.ext.database import db


employees = Blueprint('employees', __name__, template_folder='templates')

@employees.get('/employees')
def index():
    employees = Employee.query.all()
    return render_template('list.html', title='Employees', employees=employees)

@employees.get('/employees/<int:id>')
def detail(id):
    employee = Employee.query.filter_by(id=id).first()
    return jsonify(employee.serializer())

@employees.get('/employees/new')
def new():
    form = EmployeeForm()
    return render_template('new.html', title='New Employee', form=form)

@employees.post('/employees/create')
def create():
    form = EmployeeForm(request.form)
    if not form.validate_on_submit():
        return redirect('employees.new')
    id = form.id.data
    name = form.name.data
    try:
        employee = Employee(id=id, name=name)
    except:
        flash('Employee already exist!')
        return redirect('home.index')
    db.session.add(employee)
    db.session.commit()
    return redirect('home.index')

@employees.get('/employees/<int:id>/edit')
def edit(id):
    employee = Employee.query.filter_by(id=id).first()
    form = EmployeeForm()
    form.id.data = employee.id
    form.name.data = employee.name
    return render_template('edit.html', id=id, form=form)

@employees.post('/employees/<id>/update')
def update(id):
    return redirect('home.index')

@employees.delete('/employees/<id>/delete')
def delete(id):
    return redirect('home.index')