from flask import Blueprint, render_template, redirect, url_for, request
from app.models import Employee
from app.ext.wtforms.forms import EmployeeForm
from app.ext.database import db

ROWS_PER_PAGE = 10


home = Blueprint('home', __name__, template_folder='templates')

@home.get('/')
def index():
    form = EmployeeForm()

    page = request.args.get('page', 1, type=int)
    employees = Employee.query.paginate(page=page, per_page=ROWS_PER_PAGE)
    # employees = Employee.query.all()
    return render_template('home/home.html', title='ID Card Manager', employees=employees, form=form)

@home.get('/<int:id>')
def switch_print(id):
    page = request.args.get('page', 1, type=int)

    employee = Employee.query.get(id)
    employee.to_print = not employee.to_print
    db.session.add(employee)
    db.session.commit()
    return redirect(url_for('home.index', page=page))
