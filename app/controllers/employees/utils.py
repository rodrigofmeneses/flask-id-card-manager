from openpyxl import load_workbook
from flask import flash, redirect, url_for

from app.models import Company


def extract_employees(file):
    dataframe = load_workbook(file)
    rows = dataframe.active.rows

    header = [cell.value for cell in next(rows)]
    employees = []
    for row in rows:
        employees.append({key: str(cell.value) for key, cell in zip(header, row)})

    for employee in employees:
        try:
            employee["company_id"] = get_company_by_name(employee["company"]).id
            del employee["company"]
            del employee[None]
        except Exception as err:
            flash(f"{err}")
            return redirect(url_for("employees.index"))

    return employees


def get_company_by_name(name):
    try:
        return Company.query.filter_by(name=name).one()
    except:
        raise Exception("Invalid Company")
