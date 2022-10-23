from flask_wtf import FlaskForm
from app.models import Company
from wtforms import StringField, IntegerField, SubmitField, SelectField, validators


class EmployeeForm(FlaskForm):
    id = IntegerField(
        'ID', 
        [validators.DataRequired()]
    )
    name = StringField(
        'Name',
        [validators.DataRequired(), validators.length(min=1, max=140)]
    )
    companies = SelectField("Companies", choices=[], coerce=int)
    save = SubmitField('Save')

    def __init__(self):
        super(EmployeeForm, self).__init__()
        self.companies.choices = [
            (c.id, c.name) for c in Company.query.all()
        ]

class CompanyForm(FlaskForm):
    id = IntegerField(
        'ID'
    )
    name = StringField(
        'Name',
        [validators.DataRequired(), validators.length(min=1, max=140)]
    )
    save = SubmitField('Save')