from . import app
from .models import db, Company, Portfolio
from flask import render_template, request, redirect, url_for, session, flash,g
from .forms import StockForm, CompanyAddForm, PortfolioCreateForm
import json
import os
import requests
from sqlalchemy.exc import DBAPIError, IntegrityError
from .auth import app

@app.add_template_global
def get_portfolio():
    """
    """
    return Portfolio.query.filter_by(g.user.id).all()

@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')


@app.route('/search', methods=['GET', 'POST'])
@login_required
def stock_search():
    form = StockForm()
    if form.validate_on_submit():
        stock_sym = form.data['stock_sym']
        # url='https://api.iextrading.com/1.0/stock/ge/company'
        url = '{}/{}/company'.format(os.environ.get('API_URL'), stock_sym)

        response = requests.get(url)
        data = json.loads(response.text)
        session['context'] = data


        return redirect(url_for('.preview_company'))

    return render_template('search.html', form=form)




@app.route('/preview', methods=['GET', 'POST'])
@login_required
def preview_company():
    """
    """
    form_context = {
        'name': session['context']['companyName'],
        'company_sym': session['context']['symbol'],
        # 'ceo': session['context']['CEO'],
        'website': session['context']['website'],
        'sector': session['context']['sector'],
        'industry': session['context']['industry'],
    }
    form = CompanyAddForm(**form_context)
    if form.validate_on_submit():
        try:
            company = Company(
                name=form.data['name'],
                company_sym=form.data['company_sym'],
                # ceo=form.data['ceo'],
                website=form.data['website'],
                sector=form.data['sector'],
                industry=form.data['industry'],
                portfolio_id=form.data['portfolio'])
            db.session.add(company)
            db.session.commit()

        except IntegrityError as e:
            # flash(form.data['name'] + ' is already in your Portfolios')
            flash(str(e.__cause__))
            return redirect(url_for('.company_detail'))
        except DBAPIError as e:
            flash(str(e.__cause__))
            return redirect ('/')
        return redirect(url_for('.company_detail'))
    return render_template(
        'preview.html',
        form=form,
        name=form_context['name'],
        symbol=form_context['company_sym'],
        # ceo=form_context['ceo'],
        website=form_context['website'],
        sector=form_context['sector'],
        industry=form_context['industry'],
    )
@app.route('/porfolio', methods=['GET','POST'])
def company_detail():
    """
    """
    form = PortfolioCreateForm()

    if form.validate_on_submit():
        try:
            portfolio = Portfolio(name=form.data['name'])
            db.session.add(portfolio)
            db.session.commit()
        except IntegrityError as e:
            # flash(form.data['name'] + ' is already in your Portfolios')
            flash(str(e.__cause__))
            return redirect(url_for('.company_detail'))
        except DBAPIError as e:
            flash(str(e.__cause__))
            return redirect ('/')
        return redirect(url_for('.stock_search'))

    companies = Company.query.all()
    return render_template('portfolio.html',companies=companies, form=form)
    # pass
