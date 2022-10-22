from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, validators


class EmployeeForm(FlaskForm):
    id = IntegerField(
        'ID', 
        [validators.DataRequired()]
    )
    name = StringField(
        'Name',
        [validators.DataRequired(), validators.length(min=1, max=140)]
    )
    save = SubmitField('Save')

class CompanyForm(FlaskForm):
    id = IntegerField(
        'ID', 
        [validators.DataRequired()]
    )
    name = StringField(
        'Name',
        [validators.DataRequired(), validators.length(min=1, max=140)]
    )
    save = SubmitField('Save')