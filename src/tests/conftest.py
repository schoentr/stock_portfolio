from src.models import User, Company, Portfolio
from src.models import db as _db
from src import app  as _app
from flask import session
import pytest
import os

@pytest.fixture()
def app(request):
    """
    """
    _app.config.from_mapping(
        TESTING = True,
        SECRETE_KEY = os.environ.get('SECRETE_KEY'),
        SQLALCHEMY_DATABASE_URI = os.getenv('TEST_DATABASE_URL'),
        SQLACHEMY_TRACK_MODIFICATIONS= False,
        WTF_CSRF_ENABLED = False,
    )

    ctx = _app.app_context()
    ctx.push()
    def teardown():
        ctx.pop()

    request.addfinalizer(teardown)
    return _app

@pytest.fixture()
def db(app, request):
    """
    """
    def teardown():
        _db.drop_all

    _db.app = app
    _db.create_all()

    request.addfinalizer(teardown)
    return _db

@pytest.fixture()
def session(db, request):
    """
    """
    connection= db.engine.connect()
    transaction = connection.begin()

    options = dict(biund=connection, binds = {})
    session = db.create_scoped_session(options=options)

    db.session = session

    def teardown():
        transaction.rollback()
        connection.close()
        session.remove()

    request.addfinalizer(teardown)
    return session

@pytest.fixture()
def client(app, db, session):
    """
    """
    client = app.test_client()
    ctx = app.app_context()
    cts.push()

    yield client
    ctx.pop()

@pytest.fixture()
def user(session):
    """
    """
    user = User(email= 'default@domain.com', password = 'password')

    session.add(user)
    session.commit()
    return user

@pytest.fixture()
def authenticated_client(client, user):
    """
    """
    portfolio = Portfolio(name = 'Default', user_id = user.id)
    session.add(portfolio)
    session.commit()
    return portfolio

@pytest.fixture()
def company(session, portfolio):
    company = Company(name = 'Microsoft',  portfolio_id ='portfolios.id',company_sym = 'MSFT', website = 'www.microsoft.com', sector = 'TECH', industry = 'PROGRAMMING')
    session.add(company)
    session.commit()
    return company
