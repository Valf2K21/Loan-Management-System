'''
    The Loan Management System is a web application for storing, managing, and viewing debtor, debt, and payment records.
    Copyright (C) 2023 Valfrid Galinato
    
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as
    published by the Free Software Foundation, either version 3 of the
    License, or (at your option) any later version.
    
    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.
    
    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''

# import dependencies
import logging
from flask import Flask, jsonify, render_template, request

# import user-created dependencies:
from functions.debt_input import debt_input
from functions.debtor_input import debtor_input
from functions.payment_input import payment_input
from functions.view_debt_history import view_debt_history
from functions.view_payment_history import view_payment_history

# configure logging to only show error-level messages
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

# create a Flask web application instance
app = Flask(__name__)

# define path to activate main system's function below
@app.route('/', methods = ['GET', 'POST'])

# create user-defined function for loan system gui
def loan_system():
    # use render_template() function to grab filled HTML template and return to display it
    return render_template('base.html')

# define path to activate debtor input data processing function below
@app.route('/debtor-processor', methods = ['GET', 'POST'])

# create user-defined function for debtor input data procesing
def debtor_processor():    
    # store javascript's submitted json in a variable
    debtor_json = request.json

    # extract received json in their respective variables
    debtor_name = debtor_json.get('debtor_name')
    debtor_age = debtor_json.get('debtor_age')
    debtor_address = debtor_json.get('debtor_address')
    debtor_phone = debtor_json.get('debtor_phone')

    # call debtor_input() function to conduct debtor input-related data processing, then store results in two variables
    toast_type, toast_message = debtor_input(debtor_name, debtor_age, debtor_address, debtor_phone)

    # convert results into json so javascript can accept them properly
    return jsonify({'type': toast_type, 'msg': toast_message})

# define path to activate debt input data processing function below
@app.route('/debt-processor', methods = ['GET', 'POST'])

# create user-defined function for debt input data processing
def debt_processor():
    # store javascript's submitted json in a variable
    debt_json = request.json

    # extract received json in their respective variables
    debt_name = debt_json.get('debt_name')
    debt_date = debt_json.get('debt_date')
    debt_amount = debt_json.get('debt_amount')
    debt_percent = debt_json.get('debt_percent')
    debt_interest = debt_json.get('debt_interest')
    debt_total = debt_json.get('debt_total')

    # call debt_input() function to conduct debt input-related data processing, then store results in two variables
    toast_type, toast_message = debt_input(debt_name, debt_date, debt_amount, debt_percent, debt_interest, debt_total)

    # convert results into json so javascript can accept them properly
    return jsonify({'type': toast_type, 'msg': toast_message})

# define path to activate payment input data processinng function below
@app.route('/payment-processor', methods = ['GET', 'POST'])

# create user-defined function for payment input data processing
def payment_processor():
    # store javascript's submitted json in a variable
    pay_json = request.json

    # extract received json in their respective variables
    pay_name = pay_json.get('pay_name')
    pay_date = pay_json.get('pay_date')
    pay_principal = pay_json.get('pay_principal')
    pay_interest = pay_json.get('pay_interest')
    pay_total = pay_json.get('pay_total')

    # call payment_input() function to conduct payment input-related data processing, then store results in two variables
    toast_type, toast_message = payment_input(pay_name, pay_date, pay_principal, pay_interest, pay_total)

    # convert results into json so javascript can accept them properly
    return jsonify({'type': toast_type, 'msg': toast_message})

# define path to activate view history data processing function below
@app.route('/history-processor', methods = ['GET', 'POST'])

# create user-defined function for payment input data processing
def history_processor():
    # store javascript's submitted json in a variable
    hist_json = request.json
    
    # extract received json in their respective variables
    hist_name = hist_json.get('hist_name')
    hist_type = hist_json.get('hist_type')

    # if-elif conditional statements to call specific functions for viewing debt and payment histories, respectively
    if hist_type == 'debt_view':
        # call view_debt_history() function to conduct debt history viewing-related data processing, then store results in five variables
        hist_headers, hist_data, toast_type, toast_message, hist_balance = view_debt_history(hist_name)

    elif hist_type == 'payment_view':
        # call view_payment_history() function to conduct payment history viewing-related data processing, then store results in five variables
        hist_headers, hist_data, toast_type, toast_message, hist_balance = view_payment_history(hist_name)

    # convert results into json so javascript can accept them properly
    return jsonify({'headerlist': hist_headers, 'datarows': hist_data, 'type': toast_type, 'msg': toast_message, 'balance': hist_balance})

# if-statement to run FLask web application instance
if __name__ == '__main__':
    print('Loan System Link: http://127.0.0.1:5000/')
    app.run()