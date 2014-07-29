# vim: set fileencoding=utf-8 :


from flask import render_template, flash, redirect, session, url_for, request, g
from flask.ext.login import login_user, logout_user, current_user, login_required
from app import app, db, lm, oid
from forms import LoginForm
from models import User


@lm.user_loader
def load_user(email):
    return User.query.get(email)


@app.before_request
def before_request():
    g.user = current_user


@app.route('/')
@app.route('/index')
@login_required
def index():
    user = g.user
    return render_template('index.html',
                            title='Home',
                           place={'place_name': u'Chińczyk', 'available': True},
                            user=user)


def places():
    user = g.user
    places = [
        {'place_name': u'Chińczyk', 'available': True},
        {'place_name': 'Troll', 'available': True},
    ]
    return render_template('places.html',
                            title='Places',
                            places=places,
                            user=user)


@app.route('/login', methods = ['GET', 'POST'])
@oid.loginhandler
def login():
    if g.user is not None and g.user.is_authenticated():
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        session['remember_me'] = form.remember_me.data
        return oid.try_login(form.openid.data, ask_for = ['nickname', 'email'])
    return render_template('login.html',
        title='Sign In',
        form=form,
        providers=app.config['OPENID_PROVIDERS'])


@app.route('/orders')
def orders():
    #orders = db.get_orders()
    orders = [
        { 'number' : '123',
          'created': '2014-07-22 10:28',
          'ends'   : '2014-07-22 11:30',
          'place'  : 'Troll'
        }
    ]
    return render_template('orders.html',
                           orders=orders)


@app.before_request
def before_request():
    g.user = current_user


@oid.after_login
def after_login(resp):
    if resp.email is None or resp.email == "":
        flash('Invalid login. Please try again.')
        return redirect(url_for('login'))
    user = User.query.filter_by(email=resp.email).first()
    if user is None:
        nickname = resp.nickname
        if nickname is None or nickname == "":
            nickname = resp.email.split('@')[0]
        user = User(email=resp.email, nickname=nickname)
        db.session.add(user)
        db.session.commit()
    remember_me = False
    if 'remember_me' in session:
        remember_me = session['remember_me']
        session.pop('remember_me', None)
    login_user(user, remember=remember_me)
    return redirect(request.args.get('next') or url_for('index'))


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
