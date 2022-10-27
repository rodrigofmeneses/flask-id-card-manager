from flask import Blueprint, render_template
from app.ext.wtforms.forms import EmployeeForm
from app.models import Employee, Company
from app.ext.database import db


checkout = Blueprint('checkout', __name__, template_folder='templates')

@checkout.get('/checkout')
def index():
    employees = Employee.query.filter_by(for_print=False).all()
    return render_template('checkout/checkout.html', title='Checkout', employees=employees)
