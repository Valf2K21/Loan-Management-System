# import dependencies
import logging
import pyodbc
import sys
from flask import Flask, render_template, jsonify

# debug: check currently-used virtual environment
print('Python Environment:', sys.prefix)

# configure logging to only show error-level messages
#log = logging.getLogger('werkzeug')
#log.setLevel(logging.ERROR)

# create a Flask web application instance
app = Flask(__name__)

# define path to activate function below
@app.route('/')

# create user-defined function for loan system to return what to display at user
def loan_system():
    # use render_template() function to grab filled HTML template and return to display it
    return render_template('base.html')

# if-statement to run FLask web application instance
if __name__ == '__main__':
    print('Loan System Link: http://127.0.0.1:5000/')
    app.run(debug = True)