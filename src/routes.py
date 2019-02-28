from . import app
from flask import render_template
import os

@app.route('/', methods=['GET'])
def hello():
    return render_template('home.html')


@app.route('/search', methods=['GET'])
def poster():
    return render_template('search.html')


@app.route('/search', methods=['POST'])
def stock_search():
    stock_sym = request.form.get('stock')
    url = '{}?token={}&symbols{}'.format(os.environ.get('API_URL'), os.environ.get('API_KEY'),stock_sym)

    return url

@app.route('/stocks')
def show_stocks():
    return render_template('stocks.html')

