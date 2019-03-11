from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, PasswordField
from wtforms.validators import DataRequired
from .models import Portfolio


class StockForm(FlaskForm):
    """
    """
    stock_sym = StringField('Stock_Symbol', validators=[DataRequired()])


class CompanyAddForm(FlaskForm):
    """
    """
    company_sym = StringField('symbol', validators=[DataRequired()])
    name = StringField('name', validators=[DataRequired()])
    industry = StringField('industry' )
    website = StringField('website' )
    sector = StringField('sector' )
    portfolio = SelectField('portfolio')
    # name = StringField('ceo', )
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.portfolio.choices= [(str(c.id),c.name) for c in Portfolio.query.all()]

class PortfolioCreateForm(FlaskForm):
    """
    """
    name = StringField('name', validators=[DataRequired()])

class AuthForm(FlaskForm):
    """
    """
    email = StringField('email', validators= [DataRequired()])
    password = PasswordField('password', validators= [DataRequired()])




