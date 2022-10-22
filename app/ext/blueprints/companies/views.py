from flask import Blueprint, render_template, request, redirect, url_for
from app.models import Company
from app.ext.wtforms.forms import CompanyForm
from app.ext.database import db

companies = Blueprint('companies', __name__, template_folder='templates')

@companies.get('/companies')
def index():
    companies = Company.query.all()
    return render_template('companies.html', title='Companies', companies=companies)

@companies.get('/companies/new')
def new():
    form = CompanyForm()
    return render_template('companies_new.html', title='New Company', form=form)

@companies.post('/companies/create')
def create():
    form = CompanyForm(request.form)
    if not form.validate_on_submit():
        return redirect(url_for('companies.new'))
    name = form.name.data
    try:
        company = Company(name=name)
    except:
        return redirect(url_for('home.index'))
    db.session.add(company)
    db.session.commit()
    return redirect(url_for('home.index'))