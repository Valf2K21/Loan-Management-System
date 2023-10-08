# import dependencies
import pyodbc
from flask import request

# function 1: retrieve user-submitted data from debt input
def debt_input(debt_name, debt_date, debt_amount, debt_percent, debt_interest, debt_total):
    # debug: print message to confirm that this function has been called
    print('DEBUG: FUNCTION debt_input CALLED SUCCESSFULLY!')

    # test: store a print command in a variable, then return it
    result = print('SUBMITTED:\nName: ', debt_name, '\nDate: ', debt_date, '\nAmount: ', debt_amount, '\nPercent: ', debt_percent, '\nInterest: ', debt_interest, '\nTotal: ', debt_total)

    return result