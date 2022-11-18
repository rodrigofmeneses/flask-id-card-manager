from flask import Blueprint, flash, render_template, redirect, url_for, request
from app.controllers.utils import extract_employees, filter_by_name_or_id
from app.ext.database import db
from app.ext.wtforms.forms import EmployeeForm, SearchForm
from app.models import Employee

ROWS_PER_PAGE = 9


employees = Blueprint("employees", __name__, template_folder="templates")


@employees.get("/employees")
def index():
    page = request.args.get("page", 1, type=int)
    search = request.args.get("search")
    form = SearchForm()

    query = Employee.query
    if search:
        query = filter_by_name_or_id(search)

    employees = query.order_by(Employee.name).paginate(
        page=page, per_page=ROWS_PER_PAGE
    )
    return render_template(
        "employees/employees.html",
        title="Employees",
        employees=employees,
        search=search,
        form=form,
    )


@employees.get("/employees/<int:id>")
def detail(id):
    employee = Employee.query.filter_by(id=id).first()
    return {"id": employee.id, "name": employee.name}


@employees.get("/employees/new")
def new():
    form = EmployeeForm()
    return render_template(
        "employees/employees_new.html", title="New Employee", form=form
    )


@employees.post("/employees/new_file")
def create_by_file():
    file = request.files["file"]
    if not file:
        flash("No file")
        return redirect(url_for("employees.index"))

    employees_data = extract_employees(file)

    try:
        employees = [Employee(**e_d) for e_d in employees_data]
        db.session.bulk_save_objects(employees)
        db.session.commit()
        flash("Succefull added Employees")
    except Exception as err:
        flash(f"{err.orig.args}")
        flash(f"Something Wrong - Invalid Data")
    finally:
        return redirect(url_for("employees.index"))


@employees.post("/employees/create")
def create():
    form = EmployeeForm()
    if not form.validate_on_submit():
        flash("Form not valid")
        return redirect(url_for("employees.new"))

    if Employee.query.filter_by(id=form.id.data).first():
        flash("Employee has exist")
        return render_template(
            "employees/employees_new.html", title="New Employee", form=form
        )

    employee = Employee(**form.employee)
    db.session.add(employee)
    db.session.commit()

    return redirect(url_for("employees.index"))


@employees.get("/employees/<int:id>/edit")
def edit(id):
    """Edit Employee"""
    employee = Employee.query.filter_by(id=id).first()

    form = EmployeeForm()
    form.employee = employee

    return render_template(
        "employees/employees_edit.html", title="Edit Employee", id=id, form=form
    )


@employees.post("/employees/<int:id>/update")
def update(id):
    """Process Edit route"""
    form = EmployeeForm()

    if form.validate_on_submit():
        Employee.query.filter_by(id=id).update(form.employee)
        db.session.commit()

    return redirect(url_for("employees.index"))


@employees.route("/employees/<int:id>/delete")
def delete(id):

    page = request.args.get("page", 1, type=int)
    search = request.args.get("search")

    Employee.query.filter_by(id=id).delete()
    db.session.commit()
    return redirect(url_for("employees.index", page=page, search=search))
