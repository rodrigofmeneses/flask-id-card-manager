from openpyxl import load_workbook
from app.models import Employee
from sqlalchemy import or_
from flask import flash, redirect, url_for

from app.models import Company


def filter_by_name_or_id(search):
    query = Employee.query.filter(
        or_(Employee.name.ilike(f"%{search}%"), Employee.id.ilike(f"%{search}%"))
    )
    return query


def extract_employees(file):
    dataframe = load_workbook(file)
    rows = dataframe["Cards"].rows

    header = [cell.value for cell in next(rows)]
    employees = []
    for row in rows:
        employees.append({key: str(cell.value) for key, cell in zip(header, row)})

    for employee in employees:
        try:
            employee["identification"] = employee["identification"].rjust(11, '0')
            employee["company_id"] = get_company_by_name(employee["company"]).id
            del employee["company"]
        except Exception as err:
            flash(f"{err}")
            return redirect(url_for("employees.index"))

    return employees


def get_company_by_name(name):
    try:
        return Company.query.filter_by(name=name).one()
    except:
        raise Exception("Invalid Company")
