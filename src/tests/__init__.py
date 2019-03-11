from src.models import User, Company, Portfolio
from src.models import db as _db
from src import app  as _app
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

