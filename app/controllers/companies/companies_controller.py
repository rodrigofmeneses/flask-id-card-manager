from flask import Blueprint, jsonify, render_template, request, redirect, url_for
from app.models import Company
from app.ext.wtforms.forms import CompanyForm
from app.ext.database import db

companies = Blueprint("companies", __name__, template_folder="templates")


@companies.get("/companies")
def index():
    companies = Company.query.all()
    return render_template(
        "companies/companies.html", title="Companies", companies=companies
    )


@companies.get("/companies/<int:id>")
def detail(id):
    company = Company.query.filter_by(id=id).first()
    return jsonify({"id": company.id, "name": company.name})


@companies.get("/companies/new")
def new():
    form = CompanyForm()
    return render_template(
        "companies/companies_new.html", title="New Company", form=form
    )


@companies.post("/companies/create")
def create():
    form = CompanyForm(request.form)
    if not form.validate_on_submit():
        return redirect(url_for("companies.new"))
    name = form.name.data
    try:
        company = Company(name=name)
    except:
        return redirect(url_for("companies.index"))
    db.session.add(company)
    db.session.commit()
    return redirect(url_for("companies.index"))


@companies.get("/companies/<int:id>/edit")
def edit(id):
    employee = Company.query.filter_by(id=id).first()
    form = CompanyForm()
    form.id.data = employee.id
    form.name.data = employee.name
    return render_template(
        "companies/companies_edit.html", title="Edit Company", id=id, form=form
    )


@companies.post("/companies/<int:id>/update")
def update(id):
    form = CompanyForm(request.form)
    if form.validate_on_submit():
        company = Company.query.filter_by(id=request.form["current_id"]).first()
        company.name = form.name.data
        db.session.add(company)
        db.session.commit()

    return redirect(url_for("companies.index"))


@companies.route("/companies/<id>/delete")
def delete(id):
    Company.query.filter_by(id=id).delete()
    db.session.commit()
    return redirect(url_for("companies.index"))
