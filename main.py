# import dependencies
import logging
import sys
from flask import Flask, render_template, request

# import user-created dependencies:
from functions.debt_input import debt_input
from functions.debtor_input import debtor_input
from functions.payment_input import payment_input
from functions.view_debt_history import view_debt_history
from functions.view_payment_history import view_payment_history

# debug: check currently-used virtual environment
print('Python Environment:', sys.prefix)

# configure logging to only show error-level messages
#log = logging.getLogger('werkzeug')
#log.setLevel(logging.ERROR)

# create a Flask web application instance
app = Flask(__name__)

# define path to activate function below
@app.route('/', methods = ['GET', 'POST'])

# create user-defined function for loan system to return what to display at user
def loan_system():
    # use request.form.get() function to retrieve value of clicked submit_button
    button_id = request.form.get('submit_button')

    # if-elif conditional statements to call specific functions for debtor, debt and payment inputs, respectively
    if button_id == 'debtor_input':
        # use request.form.get() function to retrieve data stored in specific input IDs
        debtor_name = request.form.get('debtor_name')
        debtor_age = request.form.get('debtor_age')
        debtor_address = request.form.get('debtor_address')
        debtor_phone = request.form.get('debtor_phone')

        # call debtor_input() function to conduct debtor input-related data processing
        debtor_input(debtor_name, debtor_age, debtor_address, debtor_phone)
    
    elif button_id == 'debt_input':
        # use request.form.get() function to retrieve data stored in specific input IDs
        debt_name = request.form.get('debt_name')
        debt_date = request.form.get('debt_date')
        debt_amount = request.form.get('debt_amount')
        debt_percent = request.form.get('debt_percent')
        debt_interest = request.form.get('debt_interest')
        debt_total = request.form.get('debt_total')

        # call debt_input() function to conduct debt input-related data processing
        debt_input(debt_name, debt_date, debt_amount, debt_percent, debt_interest, debt_total)

    elif button_id == 'payment_input':
        # use request.form.get() function to retrieve data stored in specific input IDs
        pay_name = request.form.get('pay_name')
        pay_date = request.form.get('pay_date')
        pay_principal = request.form.get('pay_principal')
        pay_interest = request.form.get('pay_interest')
        pay_total = request.form.get('pay_total')

        # call payment_input() function to conduct payment input-related data processing
        payment_input(pay_name, pay_date, pay_principal, pay_interest, pay_total)
        
    elif button_id == 'view_history':
        # use request.form.get() function to retrieve data stored in specific input IDs
        hist_name = request.form.get('hist_name')
        hist_type = request.form.get('hist_type')

        # if-elif conditional statements to call specific functions for viewing debt and payment histories, respectively
        if hist_type == 'debt_view':
            # call view_debt_history() function to conduct debt history viewing-related data processing
            hist_data, running_balance = view_debt_history(hist_name)

            # use render_template() function to grab filled HTML template and return to display it
            return render_template('child-hist-debt.html', hist_data = hist_data, running_balance = running_balance[0])
        elif hist_type == 'payment_view':
            # call view_payment_history() function to conduct payment history viewing-related data processing
            hist_data, running_balance = view_payment_history(hist_name)

            # use render_template() function to grab filled HTML template and return to display it
            return render_template('child-hist-payment.html', hist_data = hist_data, running_balance = running_balance[0])

    # use render_template() function to grab filled HTML template and return to display it
    return render_template('base.html')

# if-statement to run FLask web application instance
if __name__ == '__main__':
    print('Loan System Link: http://127.0.0.1:5000/')
    app.run(debug = True)