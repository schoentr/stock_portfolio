from flask_sqlalchemy import SQLAlchemy
from datetime import datetime as dt
from flask_migrate import Migrate
from . import app


db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Stocks(db.Model):
    __tablename__ = 'stocks'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), index=True, unique=True)
    company_sym = db.Column(db.String(256), index=True, unique=True)
    latest_price = db.Column(db.String(256), index=True)
    date_created = db.Column(db.DateTime, default=dt.now())

    def __repr__(self):
        return '<company {}-{}-${}>'.format(self.name, self.company_sym, self.latest_price)
