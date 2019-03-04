from . import app
from .models import db, Company
from flask import render_template, request, redirect, url_for
import json
import os
import requests
from sqlalchemy.exc import DBAPIError, IntegrityError


@app.route('/', methods=['GET'])
def hello():
    return render_template('home.html')


@app.route('/search', methods=['GET'])
def search():
    return render_template('search.html')


@app.route('/search', methods=['POST'])
def stock_search():
    stock_sym = request.form.get('stock')
    url = '{}{}/quote?token={}'.format(os.environ.get('API_URL'),stock_sym, os.environ.get('API_KEY'))

    response = requests.get(url)
    data = json.loads(response.text)

    # return str(data)
    try:
        company = Company(
            company_sym=data['symbol'], name=data['companyName'], latest_price=data['latestPrice'])
        db.session.add(company)
        db.session.commit()
    except (DBAPIError, IntegrityError):
         abort(400)
    return redirect(url_for('.portfolio'))  


@app.route('/portfolio')
def portfolio():
    # return render_template('home.html')
    # print(Company.query.all())
    return render_template('portfolio.html')
    # pass
