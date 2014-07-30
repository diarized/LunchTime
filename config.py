import os
basedir = os.path.abspath(os.path.dirname(__file__))
DB_FILE_NAME='lunchtime.db'

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, DB_FILE_NAME)
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

CSRF_ENABLED = True
SECRET_KEY = '03b1e8f0675f051905b22a15b2ffb83f'

OPENID_PROVIDERS = [
    { 'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id' },
    { 'name': 'Yahoo', 'url': 'https://me.yahoo.com' },
    { 'name': 'AOL', 'url': 'http://openid.aol.com/<username>' },
    { 'name': 'Flickr', 'url': 'http://www.flickr.com/<username>' },
    { 'name': 'MyOpenID', 'url': 'https://www.myopenid.com' }]


# mail server settings
MAIL_SERVER = 'localhost'
MAIL_PORT = 25
MAIL_USERNAME = None
MAIL_PASSWORD = None


# administrator list
ADMINS = ['artur@monitor.stonith.pl']
