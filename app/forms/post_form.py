from flask_wtf import FlaskForm
from wtforms import StringField, HiddenField
from wtforms.validators import DataRequired

class MakePost(FlaskForm):
    title = StringField('title', validators=[DataRequired()])
    body = StringField('body', validators=[DataRequired()])
    franchise = HiddenField('franchise')