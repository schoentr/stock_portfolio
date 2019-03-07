from flask_sqlalchemy import SQLAlchemy
# from datetime import datetime as dt
from flask_migrate import Migrate
from . import app


db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Company(db.Model):
    __tablename__ = 'company'

    id = db.Column(db.Integer, primary_key=True)
    portfolio_id = db.Column(db.ForeignKey('portfolio.id'),nullable=False)
    name = db.Column(db.String(256), index=True, unique=True)
    company_sym = db.Column(db.String(256), index=True, unique=True)
    website = db.Column(db.String(256), index=True, unique=True)
    sector = db.Column(db.String(256), index=True, unique=True)
    industry = db.Column(db.String(256), index=True, unique=True)


    def __repr__(self):
        return '<Company {}-{}-{}-{}-{}>'.format(self.name, self.company_sym, self.website, self.sector, self.industry)

class Portfolio(db.Model):
    __tablename__ = 'portfolio'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), index=True)

    companies = db.relationship('Company', backref='portfolio', lazy=True)

    # date_created = db.Column(db.DateTime, default=dt.now())

    def __repr__(self):
        return '<Portfolio {}>'.format(self.name)
