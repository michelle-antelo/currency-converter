from flask import Flask, request, render_template, flash, redirect
from helpers import convert_currency, get_symbol, validate_inputs

app = Flask(__name__)

app.config['SECRET_KEY'] = "a secret!"

@app.route('/')
def homepage():
    """Homepage"""

    return render_template("converter.html")

@app.route('/result', methods =["GET", "POST"])
def result():
    """Currency Result"""
    if request.method == "POST" :
        conv_from = request.form.get('conv-from').upper()
        conv_to = request.form.get('conv-to').upper()
        invalid_Inputs = validate_inputs(conv_from, conv_to)

        if len(invalid_Inputs) <= 0:
            amount =  convert_currency(conv_from, conv_to, request.form.get('amount'))
            symbol = get_symbol(conv_to)
            return render_template("result.html", amount=amount, symbol=symbol)
        else:
            for x in invalid_Inputs:
                flash(x)
            return redirect('/')
            