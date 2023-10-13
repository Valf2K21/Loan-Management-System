# import dependencies
import psycopg2
import pandas as pd

# import user-created dependencies
from .config import config

# function 1: retrieve user-submitted data from debt input
def debt_input(debt_name, debt_date, debt_amount, debt_percent, debt_interest, debt_total):
    # debug: print message to confirm that this function has been called
    print('DEBUG: FUNCTION debt_input CALLED SUCCESSFULLY!')

    # call config() function and store results in a variable
    params = config()

    # use psycopg2.connect() function to connect to stated PostgreSQL server
    # note: ** means we want to extract the values of the returned dictionary stored in parans variable
    conn = psycopg2.connect(**params)

    # use conn.cursor() function to create a cursor for SQL command execution
    c = conn.cursor()

    # use created cursor to check if user-inputted name is already in the tb_debtor_records table
    c.execute('SELECT id FROM tb_debtor_records WHERE name = %s', (debt_name, ))

    # fetch data gathered by the cursor
    debtor_id = c.fetchone()

    # use created cursor to add new data into tb_debt_records table
    c.execute('INSERT INTO tb_debt_records(debtor_id, debt_date, debt_amount, interest_rate, interest_amount, total_debt) VALUES(%s, %s, %s, %s, %s, %s)', (debtor_id, debt_date, debt_amount, debt_percent, debt_interest, debt_total, ))
    print('NEW DATA ADDED INTO DEBT RECORDS SUCCESSFULLY!')

    # use created cursor to check if user-inputted name has existing balance record in tb_balance_records already
    c.execute('SELECT id, running_balance FROM tb_balance_records WHERE debtor_id = %s', (debtor_id, ))

    # fetch data gathered by the cursor
    balance_data = c.fetchone()

    # if-elif statement to check if the query returned a record that matches debtor_id
    if balance_data is None:
        # use created cursor to add new data into tb_balance_records table
        c.execute('INSERT INTO tb_balance_records(debtor_id, running_balance) VALUES(%s, %s)', (debtor_id, debt_total))
        print('NEW DATA ADDED INTO BALANCE RECORDS SUCCESSFULLY!')
    
    elif balance_data is not None:
        # update running balance by adding debt_total and running_balance
        new_balance = int(balance_data[1]) + int(debt_total)
        
        # use created cursor to update name's existing record from tb_balance_records table
        c.execute('UPDATE tb_balance_records SET running_balance = %s WHERE id = %s', (new_balance, balance_data[0]))
        print('NAME EXISTS IN BALANCE RECORDS AND ITS RECORD UPDATED SUCCESSFULLY!')

    # commit changes to the database
    conn.commit()

    # close cursor and connect objects after the process
    c.close()
    conn.close()