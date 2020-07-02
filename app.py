from flask import Flask, render_template, request, redirect, flash, session, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from forex_python.converter import CurrencyRates, CurrencyCodes

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey'
app.debug  = True
debug = DebugToolbarExtension(app)

currency = CurrencyRates()
symbol = CurrencyCodes()

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/convert')
def convert():
    valFrom = request.args.get('valFrom').upper()
    valTo = request.args.get('valTo').upper()
    if symbol.get_symbol(valFrom) == None or symbol.get_symbol(valTo) == None:
        flash('Check for valid currency codes')
        return redirect('/')
    valAmount = request.args.get('valAmount', None)
    if valAmount == None or valAmount == '':
        flash('check that amount is entered')
        return redirect('/')
    elif int(valAmount) <= 0:
        flash('check that amount is positive')
        return redirect('/')
    xchange = currency.convert(valFrom, valTo, float(valAmount))
    xchange = format(xchange, '.2f')
    xchangeSymbol = symbol.get_symbol(valTo)
    return render_template('convert.html', convertedValue = xchange, valueSymbol = xchangeSymbol)