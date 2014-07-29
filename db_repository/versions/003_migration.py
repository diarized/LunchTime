from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
order = Table('order', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('owner', VARCHAR(length=64)),
    Column('place', VARCHAR(length=256)),
    Column('created', DATETIME),
    Column('expires', DATETIME),
)

event = Table('event', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('owner', String(length=64)),
    Column('place', String(length=256)),
    Column('created', DateTime),
    Column('expires', DateTime),
)

ordered_meal = Table('ordered_meal', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('order_id', INTEGER),
    Column('user', VARCHAR(length=64)),
    Column('meal_id', INTEGER),
)

ordered_meal = Table('ordered_meal', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('event_id', Integer),
    Column('user', String(length=64)),
    Column('meal_id', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['order'].drop()
    post_meta.tables['event'].create()
    pre_meta.tables['ordered_meal'].columns['order_id'].drop()
    post_meta.tables['ordered_meal'].columns['event_id'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['order'].create()
    post_meta.tables['event'].drop()
    pre_meta.tables['ordered_meal'].columns['order_id'].create()
    post_meta.tables['ordered_meal'].columns['event_id'].drop()
