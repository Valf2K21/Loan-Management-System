# import dependencies
import psycopg2

# import user-created dependencies
from .config import config

# create a function to process user-submitted data from view history
def view_payment_history(hist_name):
    # call config() function and store server parameters in a variable
    params = config()

    # use psycopg2.connect() function to connect to PostgreSQL server
    # note: ** means we want to extract the values of the returned dictionary stored in parans variable
    conn = psycopg2.connect(**params)

    # use conn.cursor() function to create a cursor for SQL command execution
    c = conn.cursor()

    # use created cursor to check if user-inputted name is already in the tb_debtor_records table
    c.execute('SELECT id FROM tb_debtor_records WHERE name = %s', (hist_name, ))

    # fetch data gathered by the cursor
    debtor_id = c.fetchone()

    # if-elif statement to check if the query returned a record that matches hist_name
    if debtor_id is None:
        # store a toast type in a variable for css styling of the toast message to be displayed
        toast_type = 'fail'

        # store a toast_message in a variable to notify user that submitted name is new; therefore, debtor data, debt data, and payment data must be submitted first before viewing payment history
        toast_message = "<img src='/static/fail-octagon.svg' class='icon fail-icon'><h3>NEW NAME DETECTED - SUBMIT DEBTOR'S DATA, DEBT DATA, AND PAYMENT DATA FIRST BEFORE VIEWING PAYMENT HISTORY</h3>"

        # set the rest of the variables required as None
        hist_headers = None
        hist_data = None
        hist_balance = None

    elif debtor_id is not None:
        # use created cursor to collect all records in tb_payment_records that matches debtor_id
        c.execute('SELECT id, payment_date, principal_paid, interest_paid, total_payment FROM tb_payment_records WHERE debtor_id = %s', (debtor_id, ))
            
        # fetch data gathered by the cursor
        hist_data = c.fetchall()

        # if-elif statement to check if the query returned a record that matches debtor_id
        if hist_data == []:
            # store a toast type in a variable for css styling of the toast message to be displayed
            toast_type = 'fail'

            # store a toast message in a variable to notify user that while submitted name exists, it has no payment records to view; therefore, debt data and payment data must be submitted first before viewing payment history
            toast_message = "<img src='/static/fail-octagon.svg' class='icon fail-icon'><h3>EXISTING NAME WITH NO PAYMENT RECORDS DETECTED - SUBMIT DEBT DATA AND PAYMENT DATA FIRST BEFORE VIEWING PAYMENT HISTORY</h3>"

            # set the rest of the variables required as None
            hist_headers = None
            hist_data = None
            hist_balance = None

        elif hist_data != []:
            # create a list of headers to use and store it in a variable
            hist_headers = ['ID', 'PAYMENT DATE', 'PRINCIPAL PAID', 'INTEREST PAID', 'TOTAL PAYMENT']

            # use created cursor to check if user-inputted name has existing balance record in tb_balance_records already
            c.execute('SELECT running_balance FROM tb_balance_records WHERE debtor_id = %s', (debtor_id, ))

            # fetch data gathered by the cursor
            hist_balance = c.fetchone()

            # store a toast type in a variable for css styling of the toast message to be displayed
            toast_type = 'success'

            # store a toast message in a variable to notify user that submitted name and their payment records exists already, and payment history table is created successfully
            toast_message = "<img src='/static/success-circle.svg' class='icon success-icon'><h3>EXISTING NAME AND THEIR PAYMENT RECORDS DETECTED - PAYMENT HISTORY TABLE CREATED SUCCESSFULLY!</h3>"

    # close cursor and connect objects after the process
    c.close()
    conn.close()

    # return results back to history_processor() function for jsonification
    return hist_headers, hist_data, toast_type, toast_message, hist_balance