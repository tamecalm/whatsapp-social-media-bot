from flask_wtf import FlaskForm
from wtforms import TextAreaField, DateTimeField
from wtforms.validators import DataRequired

class SchedulePostForm(FlaskForm):
    content = TextAreaField('Content', validators=[DataRequired()])
    time = DateTimeField('Scheduled Time', validators=[DataRequired()], format='%Y-%m-%dT%H:%M')
