from flask import Blueprint, render_template
from app.ext.wtforms.forms import EmployeeForm
from app.models import Employee, Company
from app.ext.database import db


checkout = Blueprint('checkout', __name__, template_folder='templates')

# company = 'FUNECE'
# id = 123
# path = f'C:/Users/rodri/OneDrive/Maré Gráfica/Clientes/LAP/Crachás/Orgaos/{company}/fotos/3x4/{id}.jpg'

@checkout.get('/checkout')
def index():
    '''Show All employees to print.'''
    employees = Employee.query.filter_by(to_print=True).all()
    return render_template('checkout/checkout.html', title='Checkout', employees=employees)
