from flask_sqlalchemy import SQLAlchemy
# from datetime import datetime as dt
from flask_migrate import Migrate
from passlib.hash import sha256_crypt
from . import app


db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Company(db.Model):
    __tablename__ = 'company'

    id = db.Column(db.Integer, primary_key=True)
    portfolio_id = db.Column(db.ForeignKey('portfolios.id'))
    name = db.Column(db.String(256), index=True, unique=True)
    company_sym = db.Column(db.String(256), index=True, unique=True)
    website = db.Column(db.String(256), index=True, unique=True)
    sector = db.Column(db.String(256), index=True, unique=True)
    industry = db.Column(db.String(256), index=True, unique=True)
    def __repr__(self):
        return '<Company {}-{}-{}-{}-{}>'.format(self.name, self.company_sym, self.website, self.sector, self.industry)

class Portfolio(db.Model):
    __tablename__ = 'portfolios'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.ForeignKey('users.id'), nullable=False)
    name = db.Column(db.String(256), index=True)
    companies = db.relationship('Company', backref='portfolio', lazy=True)
    # date_created = db.Column(db.DateTime, default=dt.now())

    def __repr__(self):
        return '<Portfolio {}>'.format(self.name)

class User(db.Model):
    __tablename__='users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(256), nullable=False, unique=True)
    password = db.Column(db.String(256), nullable=False )
    portfolios =db.relationship('Portfolio', backref='user',lazy = True)

    def __repr__(self):
        return '<User {}'.format(self.email)

    def __init__(self,email, password):
        self.email = email
        self.password = sha256_crypt.hash(password)
    @classmethod
    def check_password_hash(cls,user,raw_password):
        if user is not None:
            if sha256_crypt.verify(raw_password,user.password):
                return True
        return False
