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
import psycopg2

# import user-created dependencies
from .config import config

# create a function to process user-submitted data from debt input
def debt_input(debt_name, debt_date, debt_amount, debt_percent, debt_interest, debt_total):
    # call config() function and store server parameters in a variable
    params = config()

    # use psycopg2.connect() function to connect to PostgreSQL server
    # note: ** means we want to extract the values of the returned dictionary stored in parans variable
    conn = psycopg2.connect(**params)

    # use conn.cursor() function to create a cursor for SQL command execution
    c = conn.cursor()

    # use created cursor to check if user-inputted name is already in the tb_debtor_records table
    c.execute('SELECT id FROM tb_debtor_records WHERE name = %s', (debt_name, ))

    # fetch data gathered by the cursor
    debtor_id = c.fetchone()

    # if-elif statement to check if the query returned a record that matches debt_name
    if debtor_id is None:
        # store a toast type in a variable for css styling of the toast message to be displayed
        toast_type = 'fail'

        # store a toast message in a variable to notify user that submitted name is new, therefore debtor data must be submitted first before submitting debt data
        toast_message = "<img src='/static/fail-octagon.svg' class='icon fail-icon'><h3>NEW NAME DETECTED - SUBMIT DEBTOR'S DATA FIRST BEFORE ADDING DEBT DATA</h3>"
    
    elif debtor_id is not None:
        # use created cursor to add new data into tb_debt_records table
        c.execute('INSERT INTO tb_debt_records(debtor_id, debt_date, debt_amount, interest_rate, interest_amount, total_debt) VALUES(%s, %s, %s, %s, %s, %s)', (debtor_id, debt_date, debt_amount, debt_percent, debt_interest, debt_total, ))

        # use created cursor to check if user-inputted name has existing balance record in tb_balance_records already
        c.execute('SELECT id, running_balance FROM tb_balance_records WHERE debtor_id = %s', (debtor_id, ))

        # fetch data gathered by the cursor
        balance_data = c.fetchone()

        # if-elif statement to check if the query returned a record that matches debtor_id
        if balance_data is None:
            # since debtor has no current balance, set debt_total as new_balance
            new_balance = debt_total

            # use created cursor to add new data into tb_balance_records table
            c.execute('INSERT INTO tb_balance_records(debtor_id, running_balance) VALUES(%s, %s)', (debtor_id, new_balance, ))
        
        elif balance_data is not None:
            # calculate new_balance by adding debt_total and running_balance
            new_balance = int(balance_data[1]) + int(debt_total)
            
            # use created cursor to update name's existing record from tb_balance_records table
            c.execute('UPDATE tb_balance_records SET running_balance = %s WHERE id = %s', (new_balance, balance_data[0], ))
        
        # store a toast type in a variable for css styling of the toast message to be displayed
        toast_type = 'success'

        # store a toast message in a variable to notify user that submitted name exists already and debt data is added successfully
        toast_message = f"<img src='/static/success-circle.svg' class='icon success-icon'><h3>EXISTING NAME DETECTED - DEBT DATA ADDED SUCCESSFULLY!</h3><br><h3>EXISTING DEBTOR'S NAME: {debt_name}</h3><br><p>DEBT DATE: {debt_date}<br>DEBT AMOUNT: {debt_amount}<br>INTEREST RATE (%): {debt_percent}<br>INTEREST AMOUNT: {debt_interest}<br>TOTAL DEBT: {debt_total}<br>RUNNING BALANCE: {new_balance}</p>"

    # commit changes to the database
    conn.commit()

    # close cursor and connect objects after the process
    c.close()
    conn.close()

    # return results back to debt_processor() function for jsonification
    return toast_type, toast_message