from . import app
# from .models import db, Stocks
from flask import render_template, request
import json
import os
import requests

@app.route('/', methods=['GET'])
def hello():
    return render_template('home.html')


@app.route('/search', methods=['GET'])
def poster():
    return render_template('search.html')


@app.route('/search', methods=['POST'])
def stock_search():
    stock_sym = request.form.get('stock')
    url ='{}{}/quote?token={}'.format(os.environ.get('API_URL'),stock_sym, os.environ.get('API_KEY'))

    response = requests.get(url)
    data = json.loads(response.text)

    return str(data)
#     try:
#         stock = Stocks(company_sym=data['symbol'],name=data[companyName],latest_price=data[latestPrice] )
#         db.session.add(stock)
#         db.session.commit()
#     except:
#         (DBAIPError, IntegrityError)
#     return redirect (url_for('.portfolio'))

@app.route('/portfolio')
def show_stocks():
    return render_template('portfolio.html')

