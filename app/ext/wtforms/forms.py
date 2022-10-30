from flask_wtf import FlaskForm
from app.models import Company
from wtforms import BooleanField, StringField, IntegerField, SubmitField, SelectField, validators


class EmployeeForm(FlaskForm):
    id = IntegerField('ID', [validators.DataRequired()])
    name = StringField('Name', [validators.DataRequired(), validators.length(min=1, max=100)])
    war_name = StringField('War Name', [validators.DataRequired(), validators.length(min=1, max=50)])
    role = StringField('Role', [validators.DataRequired(), validators.length(min=1, max=50)])
    identification = StringField('Identification', [validators.DataRequired(), validators.length(min=1, max=13)])
    admission = StringField('Admission Date', [validators.DataRequired(), validators.length(min=1, max=10)])
    company = SelectField("Company", choices=[], coerce=int)
    to_print = BooleanField('To Print')
    save = SubmitField('Save')

    def __init__(self):
        super(EmployeeForm, self).__init__()
        self.company.choices = [
            (c.id, c.name) for c in Company.query.all()
        ]

class CompanyForm(FlaskForm):
    id = IntegerField('ID')
    name = StringField('Name', [validators.DataRequired(), validators.length(min=1, max=140)])
    save = SubmitField('Save')