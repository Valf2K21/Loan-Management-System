# import dependencies
import psycopg2

# import user-created dependencies
from .config import config

# function 1: retrieve user-submitted data from view history
def view_debt_history(hist_name):
    # debug: print message to confirm that this function has been called
    print('DEBUG: FUNCTION view_debt_history CALLED SUCCESSFULLY!')

    # call config() function and store results in a variable
    params = config()

    # use psycopg2.connect() function to connect to stated PostgreSQL server
    # note: ** means we want to extract the values of the returned dictionary stored in parans variable
    conn = psycopg2.connect(**params)

    # use conn.cursor() function to create a cursor for SQL command execution
    c = conn.cursor()

    # use created cursor to check if user-inputted name is already in the tb_debtor_records table
    c.execute('SELECT id FROM tb_debtor_records WHERE name = %s', (hist_name, ))

    # fetch data gathered by the cursor
    debtor_id = c.fetchone()

    # use created cursor to collect all records in tb_debt_records that matches debtor_id
    c.execute('SELECT id, debt_date, debt_amount, interest_rate, interest_amount, total_debt FROM tb_debt_records WHERE debtor_id = %s', (debtor_id, ))

    # fetch data gathered by the cursor
    hist_data = c.fetchall()

    # use created cursor to check if user-inputted name has existing balance record in tb_balance_records already
    c.execute('SELECT running_balance FROM tb_balance_records WHERE debtor_id = %s', (debtor_id, ))

    # fetch data gathered by the cursor
    running_balance = c.fetchone()

    return hist_data, running_balance