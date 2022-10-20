from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators


class EmployeeForm(FlaskForm):
    id = StringField(
        'ID', 
        [validators.DataRequired(), validators.length(min=1, max=6)]
    )
    name = StringField(
        'Name',
        [validators.DataRequired(), validators.length(min=1, max=140)]
    )
    save = SubmitField('Save')