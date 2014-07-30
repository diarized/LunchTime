from flask.ext.wtf import Form
from wtforms import TextField, BooleanField
from wtforms.validators import DataRequired
import time


class LoginForm(Form):
    openid = TextField('openid', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)


class NewPlaceForm(Form):
    name = TextField('name', validators=[DataRequired()])
    description = TextField('description', validators=[DataRequired()])


class NewEventForm(Form):
    place_name = TextField('place_name', validators=[DataRequired()])
    expires = TextField('expires', validators=[DataRequired()])

    def validate(self):
        if not Form.validate(self):
            return False
        now = dict(
            zip(
                ['year', 'month', 'day', 'hour', 'minute', 'second', 'day_of_week', 'day_of_year', 'is_dst'],
                [x for x in time.localtime()]
            )
        )
        # [2014, 7, 30, 23, 8, 38, 2, 211, 1]
        try:
            hour_exp, minute_exp = [int(t) for t in self.expires.data.split(":")]
        except ValueError:
            self.expires.errors.append('Please enter hour:minute in the near future.')
            return False
        if hour_exp < 8 or hour_exp > 18:
            self.expires.errors.append('Please enter time within working hours.')
            return False
        if minute_exp < 0 or minute_exp > 59:
            self.expires.errors.append('Please enter valid number for minutes.')
            return False
        return True


class NewMealForm(Form):
    name = TextField('name', validators=[DataRequired()])
    description = TextField('description', validators=[DataRequired()])
    price = TextField('price', validators=[DataRequired()])
