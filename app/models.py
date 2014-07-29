from app import db


class User(db.Model):
    email = db.Column(db.String(120), primary_key=True)
    nickname = db.Column(db.String(64), unique = True)
    posts = db.relationship('Post', backref = 'author', lazy = 'dynamic')

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.email)


class Place(db.Model):
    place_name = db.Column(db.String(256), primary_key=True)
    available = db.Column(db.Boolean)

    def __repr__(self):
        return "<Place %r>" % (self.name)


class Meal(db.Model):
    id          = db.Column(db.Integer,      primary_key=True)
    meal_name   = db.Column(db.String(256),  index=True      )
    description = db.Column(db.String(1024)                  )

    def __repr__(self):
        return "<Meal %r>" % (self.name)


class Event(db.Model):
    id    = db.Column(db.Integer,     primary_key=True)
    owner = db.Column(db.String(64),  db.ForeignKey('user.nickname'))
    place = db.Column(db.String(256), db.ForeignKey('place.place_name'))
    created = db.Column(db.DateTime)
    expires = db.Column(db.DateTime)

    def __repr__(self):
        return "<Event at %s created by %r>" % (self.place, self.owner)


class OrderedMeal(db.Model):
    id       = db.Column(db.Integer,    primary_key=True)
    event_id = db.Column(db.Integer,    db.ForeignKey('event.id'))
    user     = db.Column(db.String(64), db.ForeignKey('user.nickname'))
    meal_id  = db.Column(db.Integer,    db.ForeignKey('meal.id'))

    def __repr__(self):
        return "<OrderedMeal %r>" % (self.meal_id)

