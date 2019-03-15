from flask_wtf  import FlaskForm
from wtforms import StringField, IntegerField, DateField
from wtforms.validators import DataRequired

class EventForm(FlaskForm):
    ID = IntegerField('ID', )
    title = StringField('tittel', validators=[DataRequired()])
    description = StringField('description')
    startDate = DateField('startDate')


