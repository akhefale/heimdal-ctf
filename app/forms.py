from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class FlagForm(FlaskForm):
    hash = StringField('Flag ID', validators=[DataRequired()])
    alias = StringField('Alias', validators=[DataRequired()])
    alias_hash = StringField('Alias Hash')
    submit = SubmitField('Aflever Flag')
