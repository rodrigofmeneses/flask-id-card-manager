from flask_wtf import FlaskForm
from app.models import Company, Employee
from wtforms import (
    BooleanField,
    StringField,
    IntegerField,
    SubmitField,
    SelectField,
    validators,
)


class EmployeeForm(FlaskForm):
    id = IntegerField("ID", [validators.DataRequired()])
    name = StringField(
        "Name", [validators.DataRequired(), validators.length(min=1, max=100)]
    )
    war_name = StringField(
        "War Name", [validators.DataRequired(), validators.length(min=1, max=50)]
    )
    role = StringField(
        "Role", [validators.DataRequired(), validators.length(min=1, max=50)]
    )
    identification = StringField(
        "Identification", [validators.DataRequired(), validators.length(min=1, max=13)]
    )
    admission = StringField(
        "Admission Date", [validators.DataRequired(), validators.length(min=1, max=10)]
    )
    company = SelectField("Company", choices=[], coerce=int)
    to_print = BooleanField("To Print")
    save = SubmitField("Save")

    def __init__(self):
        super(EmployeeForm, self).__init__()
        self.company.choices = [(c.id, c.name) for c in Company.query.all()]

    @property
    def employee(self):
        data = self.data
        data["company_id"] = self.company.data
        del data["save"]
        del data["company"]
        del data["csrf_token"]
        return data

    @employee.setter
    def employee(self, employee: Employee):
        self.id.data = employee.id
        self.name.data = employee.name
        self.war_name.data = employee.war_name
        self.role.data = employee.role
        self.identification.data = employee.identification
        self.admission.data = employee.admission
        self.company.data = employee.company
        self.to_print.data = employee.to_print


class CompanyForm(FlaskForm):
    id = IntegerField("ID")
    name = StringField(
        "Name", [validators.DataRequired(), validators.length(min=1, max=140)]
    )
    save = SubmitField("Save")


class SearchForm(FlaskForm):
    search = StringField("Filter by ID or Name")
