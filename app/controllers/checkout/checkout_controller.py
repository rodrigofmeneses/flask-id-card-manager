from flask import Blueprint, render_template, request, send_file
from app.models import Employee

import csv

ROWS_PER_PAGE = 15


checkout = Blueprint("checkout", __name__, template_folder="templates")


@checkout.get("/checkout")
def index():
    """Show All employees to print."""
    page = request.args.get("page", 1, type=int)

    query = Employee.query.filter_by(to_print=True).order_by(Employee.name)
    employees = query.paginate(page=page, per_page=ROWS_PER_PAGE)
    return render_template(
        "checkout/checkout.html", title="Checkout", employees=employees
    )


@checkout.get("/checkout/download_front/")
def download_front():
    """Create and download front file based on employees to print"""
    employees = Employee.query.filter_by(to_print=True).all()

    with open("app/tmp/front.csv", "w", encoding="UTF8", newline="") as file:
        data = file_front(employees)
        writer = csv.writer(file)
        writer.writerows(data)

    return send_file(
        "tmp/front.csv",
        mimetype="text/csv",
        download_name="front.csv",
        as_attachment=True,
    )


@checkout.get("/checkout/download_back/")
def download_back():
    """Create and download back file based on employees to print"""
    employees = Employee.query.filter_by(to_print=True).all()

    with open("app/tmp/back.csv", "w", encoding="UTF8", newline="") as file:
        data = file_back(employees)
        writer = csv.writer(file)
        writer.writerows(data)

    return send_file(
        "tmp/back.csv",
        mimetype="text/csv",
        download_name="back.csv",
        as_attachment=True,
    )


def file_front(employees) -> str:
    data = [["matricula", "nome_guerra", "cargo", "lotacao", "foto", "mostrar_foto"]]
    for employee in employees:
        data.append(
            [
                employee.id,
                employee.war_name,
                employee.role,
                employee.company.name,
                f"C:/Users/Mareg/OneDrive/Maré Gráfica/Clientes/LAP/Crachás/Orgaos/{employee.company.name}/fotos/3x4/{employee.id}.jpg",
                "True",
            ]
        )
    return data


def file_back(employees) -> str:
    data = [["matricula", "nome", "identidade", "admissao"]]
    for employee in employees:
        data.append(
            [employee.id, employee.name, employee.identification, employee.admission]
        )
    return data
