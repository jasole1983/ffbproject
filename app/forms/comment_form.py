from flask_wtf import FlaskForm
from wtforms import StringField, HiddenField
from wtforms.validators import DataRequired
import time

class MakeComment(FlaskForm):
    post = HiddenField('post')
    body = StringField('body', validators=[DataRequired()])
    franchise = HiddenField('franchise')
    modify_date = time.time()