from flask import Blueprint, render_template
from app.models import Employee


home = Blueprint('home', __name__, template_folder='templates')

@home.get('/')
def index():
    employees = Employee.query.all()
    return render_template('home.html', title='ID Card Manager', employees=employees)