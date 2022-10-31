from flask import Blueprint, render_template, redirect, url_for
from app.models import Company, Employee
from app.ext.wtforms.forms import EmployeeForm
from app.ext.database import db


home = Blueprint('home', __name__, template_folder='templates')

@home.get('/')
def index():
    form = EmployeeForm()
    employees = Employee.query.all()
    return render_template('home/home.html', title='ID Card Manager', employees=employees, form=form)

@home.get('/<int:id>')
def switch_print(id):
    employee = Employee.query.get(id)
    employee.to_print = not employee.to_print
    db.session.add(employee)
    db.session.commit()
    return redirect(url_for('home.index'))
