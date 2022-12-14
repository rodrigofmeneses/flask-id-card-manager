from flask import Blueprint, render_template, redirect, url_for, request
from app.models import Employee
from app.ext.wtforms.forms import SearchForm
from app.ext.database import db
from app.controllers.utils import filter_by_name_or_id

ROWS_PER_PAGE = 9


home = Blueprint("home", __name__, template_folder="templates")


@home.get("/")
def index():
    page = request.args.get("page", 1, type=int)
    search = request.args.get("search")
    form = SearchForm(request.args, meta={"csrf": False})

    query = Employee.query
    if search:
        query = filter_by_name_or_id(search)

    employees = query.order_by(Employee.name).paginate(
        page=page, per_page=ROWS_PER_PAGE
    )
    return render_template(
        "home/home.html",
        title="ID Card Manager",
        employees=employees,
        search=search,
        form=form,
    )

@home.get('/not-to-print/')
def not_to_print():
    for employee in Employee.query.all():
        employee.to_print = False
    db.session.commit()
    return redirect(url_for('home.index'))

@home.get("/<int:id>/")
def switch_print(id):
    page = request.args.get("page", 1, type=int)
    search = request.args.get("search", type=str)

    employee = Employee.query.get(id)
    employee.to_print = not employee.to_print
    db.session.add(employee)
    db.session.commit()
    return redirect(url_for("home.index", page=page, search=search))
