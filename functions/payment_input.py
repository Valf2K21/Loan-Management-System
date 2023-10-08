# import dependencies
import pyodbc
from flask import request

# function 1: retrieve user-submitted data from payment input
def payment_input(pay_name, pay_date, pay_principal, pay_interest, pay_total):
    # debug: print message to confirm that this function has been called
    print('DEBUG: FUNCTION payment_input CALLED SUCCESSFULLY!')

    # test: store a print command in a variable, then return it
    result = print('SUBMITTED:\nName: ', pay_name, '\nDate: ', pay_date, '\nPrincipal: ', pay_principal, '\nInterest: ', pay_interest, '\nTotal: ', pay_total)

    return result