from flask.ext.wtf import Form
from wtforms import TextField, BooleanField, SelectField
from wtforms.validators import DataRequired
from models import Place
from dateutil import parser as timeparser
import datetime


class LoginForm(Form):
    openid = TextField('openid', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)


class NewPlaceForm(Form):
    name = TextField('name', validators=[DataRequired()])
    description = TextField('description', validators=[DataRequired()])


class NewEventForm(Form):
    places = Place.query.filter_by(available=True) # mandatory for validation
    place_name = SelectField('place_name', choices=places, validators=[DataRequired()])
    expires = TextField('expires', validators=[DataRequired()])

    def validate(self):
        if not Form.validate(self):
            return False
        end_of_event = timeparser.parse(self.expires.data)
        time_given = timeparser.parse(end_of_event) - datetime.datetime.now()
        min_time_window = datetime.timedelta(0, 3600)
        if time_given < min_time_window:
            self.expires.errors.append(
                'Please enter valid time and give at least an hour to others.'
            )
            return False
        return True


class NewMealForm(Form):
    name = TextField('name', validators=[DataRequired()])
    description = TextField('description', validators=[DataRequired()])
    price = TextField('price', validators=[DataRequired()])
