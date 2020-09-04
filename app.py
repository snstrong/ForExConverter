"""Flask app for routing forex converter project"""
from flask import Flask, request, render_template, redirect, session, jsonify, flash
from flask_debugtoolbar import DebugToolbarExtension
import converter
from forex_python.converter import RatesNotAvailableError
from decimal import Decimal

app = Flask(__name__)
app.config['SECRET_KEY'] = "very-very-secret"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

@app.route('/')
def show_converter():
    """Shows home page"""
    return render_template('index.html')

@app.route('/result')
def convert_currency():
    """Calls conversion functions on query args and displays results"""
    convert_from = request.args['convert-from']
    convert_to = request.args['convert-to']
    starting_amount = round(Decimal(request.args['amount']), 2)
    c = converter.Converter()
    try:
        if not c.validate_currency_code(convert_from):
            flash(f'Invalid currency code: {convert_from}')
            return redirect('/')
        if not c.validate_currency_code(convert_to):
            flash(f"Invalid currency code: {convert_to}")
            return redirect('/')
        converted_amount = c.convert_currency(convert_from, convert_to, starting_amount)
        curr_symbol_1 = c.forex_codes.get_symbol(convert_from)
        curr_symbol_2 = c.forex_codes.get_symbol(convert_to)
        return render_template('result.html', convert_from=convert_from, convert_to=convert_to, starting_amount=starting_amount, converted_amount=converted_amount, symbol_1=curr_symbol_1, symbol_2=curr_symbol_2)
    except RatesNotAvailableError(err):
        flash(err)
        redirect('/')