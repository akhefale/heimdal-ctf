from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class FlagForm(FlaskForm):
    hash = StringField('Flag ID', validators=[DataRequired()])
    alias = StringField('Alias', validators=[DataRequired()])
    submit = SubmitField('Aflever Flag')
