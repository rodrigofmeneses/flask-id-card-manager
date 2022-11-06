from flask import Blueprint, flash, jsonify, render_template, redirect, url_for, request
from app.ext.wtforms.forms import EmployeeForm
from app.models import Employee, Company
from app.ext.database import db

from .utils import extract_employees


employees = Blueprint('employees', __name__, template_folder='templates')

@employees.get('/employees')
def index():
    employees = Employee.query.all()
    return render_template('employees/employees.html', title='Employees', employees=employees)

@employees.get('/employees/<int:id>')
def detail(id):
    employee = Employee.query.filter_by(id=id).first()
    return {'id':employee.id, 'name':employee.name}

@employees.get('/employees/new')
def new():
    form = EmployeeForm()
    return render_template('employees/employees_new.html', title='New Employee', form=form)

@employees.post('/employees/new_file')
def create_by_file():
    file = request.files['file']
    if not file:
        flash('No file')
        return redirect(url_for('employees.index'))

    employees_data = extract_employees(file)

    employees = [Employee(**e_d) for e_d in employees_data]

    try:
        db.session.bulk_save_objects(employees)
        db.session.commit()
        flash('Succefull added Employees')
    except:
        flash('Something Wrong - Invalid Data')
    finally:
        return redirect(url_for('employees.index'))


@employees.post('/employees/create')
def create():
    form = EmployeeForm()
    if not form.validate_on_submit():
        flash('Form not valid')
        return redirect(url_for('employees.new'))

    if Employee.query.filter_by(id=form.id.data).first():
        flash('Employee has exist')
        return render_template('employees/employees_new.html', title='New Employee', form=form)
    
    employee = Employee(**form.employee_dict())
    db.session.add(employee)
    db.session.commit()

    return redirect(url_for('employees.index'))

@employees.get('/employees/<int:id>/edit')
def edit(id):
    employee = Employee.query.filter_by(id=id).first()
    form = EmployeeForm()
    form.employee = employee
    return render_template('employees/employees_edit.html', title='Edit Employee', id=id, form=form)

@employees.post('/employees/<int:id>/update')
def update(id):
    form = EmployeeForm()
    if form.validate_on_submit():
        Employee.query.filter_by(id=id).update(form.employee)
        db.session.commit()

    return redirect(url_for('employees.index'))

@employees.route('/employees/<int:id>/delete')
def delete(id):
    Employee.query.filter_by(id=id).delete()
    db.session.commit()
    return redirect(url_for('employees.index'))