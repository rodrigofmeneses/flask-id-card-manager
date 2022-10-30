from flask import Blueprint, flash, jsonify, render_template, redirect, url_for
from app.ext.wtforms.forms import EmployeeForm
from app.models import Employee, Company
from app.ext.database import db


employees = Blueprint('employees', __name__, template_folder='templates')

@employees.get('/employees')
def index():
    employees = Employee.query.all()
    return render_template('employees/employees.html', title='Employees', employees=employees)

@employees.get('/employees/<int:id>')
def detail(id):
    employee = Employee.query.filter_by(id=id).first()
    return jsonify({'id':employee.id, 'name':employee.name})

@employees.get('/employees/new')
def new():
    form = EmployeeForm()
    return render_template('employees/employees_new.html', title='New Employee', form=form)

@employees.post('/employees/create')
def create():
    form = EmployeeForm()
    if not form.validate_on_submit():
        flash('Form not valid')
        return redirect(url_for('employees.new'))
    id = form.id.data
    name = form.name.data
    war_name = form.war_name.data
    role = form.role.data
    identification = form.identification.data
    admission = form.admission.data
    company_id = form.company.data
    to_print = form.to_print.data

    if Employee.query.filter_by(id=id).first():
        flash('Employee has exist')
        return render_template('employees/employees_new.html', title='New Employee', form=form)
    employee = Employee(
            id=id, 
            name=name,
            war_name=war_name,
            role=role,
            identification=identification,
            admission=admission,
            company_id=company_id,
            to_print=to_print
        )
    db.session.add(employee)
    db.session.commit()

    return redirect(url_for('employees.index'))

@employees.get('/employees/<int:id>/edit')
def edit(id):
    employee = Employee.query.filter_by(id=id).first()
    form = EmployeeForm()
    form.id.data = employee.id
    form.name.data = employee.name
    form.war_name.data = employee.war_name
    form.role.data = employee.role
    form.identification.data = employee.identification
    form.admission.data = employee.admission
    form.company.data = employee.company
    return render_template('employees/employees_edit.html', title='Edit Employee', id=id, form=form)

@employees.post('/employees/<int:id>/update')
def update(id):
    form = EmployeeForm()
    if form.validate_on_submit():
        employee = Employee.query.get(id)
        employee.id = form.id.data
        employee.name = form.name.data
        employee.war_name = form.war_name.data
        employee.role = form.role.data
        employee.identification = form.identification.data
        employee.admission = form.admission.data
        employee.to_print = form.to_print.data
        employee.company = Company.query.get(form.company.data)
        db.session.add(employee)
        db.session.commit()

    return redirect(url_for('employees.index'))

@employees.route('/employees/<id>/delete')
def delete(id):
    Employee.query.filter_by(id=id).delete()
    db.session.commit()
    return redirect(url_for('employees.index'))