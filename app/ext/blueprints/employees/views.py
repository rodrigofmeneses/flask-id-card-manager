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
        return redirect(url_for('employees.new'))
    id = form.id.data
    name = form.name.data
    try:
        employee = Employee(id=id, name=name)
    except:
        flash('Employee already exist!')
        return redirect(url_for('home.index'))
    db.session.add(employee)
    db.session.commit()
    return redirect(url_for('home.index'))

@employees.get('/employees/<id>/edit')
def edit(id):
    employee = Employee.query.filter_by(id=id).first()
    form = EmployeeForm()
    form.id.data = employee.id
    form.name.data = employee.name
    return render_template('edit.html', id=id, form=form)

@employees.post('/employees/<id>/update')
def update(id):
    form = EmployeeForm(request.form)
    if form.validate_on_submit():
        employee = Employee.query.filter_by(id=form.id.data).first()
        employee.name = form.name.data
        employee.id = form.id.data

        db.session.add(employee)
        db.session.commit()

    return redirect(url_for('home.index'))

@employees.route('/employees/<id>/delete')
def delete(id):
    Employee.query.filter_by(id=id).delete()
    db.session.commit()
    return redirect(url_for('home.index'))