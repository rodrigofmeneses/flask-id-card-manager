from flask import Blueprint, flash, redirect, render_template, url_for
from app.models import Employee
from app.ext.database import db

import csv


checkout = Blueprint('checkout', __name__, template_folder='templates')

@checkout.get('/checkout')
def index():
    '''Show All employees to print.'''
    employees = Employee.query.filter_by(to_print=True).all()
    return render_template('checkout/checkout.html', title='Checkout', employees=employees)

@checkout.get('/checkout/export')
def export_file():
    employees = Employee.query.filter_by(to_print=True).all()
    
    with open('app/tmp/tmp_front.csv', 'w', encoding='UTF8', newline='') as file:
        data = file_front(employees)
        writer = csv.writer(file)
        writer.writerows(data)
    
    with open('app/tmp/tmp_back.csv', 'w', encoding='UTF8', newline='') as file:
        data = file_back(employees)
        writer = csv.writer(file)
        writer.writerows(data)

    flash('Files export to path app/tmp/')

    return redirect(url_for('checkout.index'))

def file_front(employees) -> str:
    data = [['matricula', 'nome_guerra' , 'cargo', 'lotacao', 'foto', 'mostrar_foto']]
    for employee in employees:
        data.append([
            employee.id,
            employee.war_name,
            employee.role,
            employee.company.name,
            f'C:/Users/rodri/OneDrive/Maré Gráfica/Clientes/LAP/Crachás/Orgaos/{employee.company.name}/fotos/3x4/{employee.id}.jpg',
            'True'
        ])
    return data

def file_back(employees) -> str:
    data = [['matricula', 'nome', 'identidade', 'admissao']]
    for employee in employees:
        data.append([
            employee.id,
            employee.name,
            employee.identification,
            employee.admission
        ])
    return data