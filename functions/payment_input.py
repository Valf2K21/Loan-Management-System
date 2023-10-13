# import dependencies
import psycopg2
import pandas as pd

# import user-created dependencies
from .config import config

# function 1: retrieve user-submitted data from payment input
def payment_input(pay_name, pay_date, pay_principal, pay_interest, pay_total):
    # debug: print message to confirm that this function has been called
    print('DEBUG: FUNCTION payment_input CALLED SUCCESSFULLY!')

    # call config() function and store results in a variable
    params = config()

    # use psycopg2.connect() function to connect to stated PostgreSQL server
    # note: ** means we want to extract the values of the returned dictionary stored in parans variable
    conn = psycopg2.connect(**params)

    # use conn.cursor() function to create a cursor for SQL command execution
    c = conn.cursor()

    # use created cursor to check if user-inputted name is already in the tb_debtor_records table
    c.execute('SELECT id FROM tb_debtor_records WHERE name = %s', (pay_name, ))

    # fetch data gathered by the cursor
    debtor_id = c.fetchone()

    # use created cursor to add new data into tb_payment_records table
    c.execute('INSERT INTO tb_payment_records(debtor_id, payment_date, principal_paid, interest_paid, total_payment) VALUES(%s, %s, %s, %s, %s)', (debtor_id, pay_date, pay_principal, pay_interest, pay_total, ))
    print('NEW DATA ADDED INTO PAYMENT RECORDS SUCCESSFULLY!')

    # use created cursor to check if user-inputted name has existing balance record in tb_balance_records already
    c.execute('SELECT id, running_balance FROM tb_balance_records WHERE debtor_id = %s', (debtor_id, ))

    # fetch data gathered by the cursor
    balance_data = c.fetchone()

    # if-elif statement to check if the query returned a record that matches debtor_id
    if balance_data is None:
        # use created cursor to add new data into tb_balance_records table
        c.execute('INSERT INTO tb_balance_records(debtor_id, running_balance) VALUES(%s, %s)', (debtor_id, pay_total))
        print('NEW DATA ADDED INTO BALANCE RECORDS SUCCESSFULLY!')

    elif balance_data is not None:
        # update running balance by subtracting pay_total and running_balance
        new_balance = int(balance_data[1]) - int(pay_total)
        
        # use created cursor to update name's existing record from tb_balance_records table
        c.execute('UPDATE tb_balance_records SET running_balance = %s WHERE id = %s', (new_balance, balance_data[0]))
        print('NAME EXISTS IN BALANCE RECORDS AND ITS RECORD UPDATED SUCCESSFULLY!')

    # commit changes to the database
    conn.commit()

    # close cursor and connect objects after the process
    c.close()
    conn.close()