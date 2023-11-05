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

# create a function to process user-submitted data from payment input
def payment_input(pay_name, pay_date, pay_principal, pay_interest, pay_total):
    # call config() function and store server parameters in a variable
    params = config()

    # use psycopg2.connect() function to connect to PostgreSQL server
    # note: ** means we want to extract the values of the returned dictionary stored in parans variable
    conn = psycopg2.connect(**params)

    # use conn.cursor() function to create a cursor for SQL command execution
    c = conn.cursor()

    # use created cursor to check if user-inputted name is already in the tb_debtor_records table
    c.execute('SELECT id FROM tb_debtor_records WHERE name = %s', (pay_name, ))

    # fetch data gathered by the cursor
    debtor_id = c.fetchone()

    # if-elif statement to check if the query returned a record that matches pay_name
    if debtor_id is None:
        # store a toast type in a variable for css styling of the toast message to be displayed
        toast_type = 'fail'

        # store a toast message in a variable to notify user that submitted name is new; therefore, debtor data and debt data must be submitted first before submitting payment data
        toast_message = "<img src='/static/fail-octagon.svg' class='icon fail-icon'><h3>NEW NAME DETECTED - SUBMIT DEBTOR'S DATA AND DEBT DATA FIRST BEFORE ADDING PAYMENT DATA</h3>"

    elif debtor_id is not None:
        # use created cursor to check if user-inputted name has existing balance record in tb_balance_records already
        c.execute('SELECT id, running_balance FROM tb_balance_records WHERE debtor_id = %s', (debtor_id, ))

        # fetch data gathered by the cursor
        balance_data = c.fetchone()

        # if-elif statement to check if the query returned a record that matches debtor_id
        if balance_data is None:
            # store a toast type in a variable for css styling of the toast message to be displayed
            toast_type = 'fail'

            # store a toast message in a variable to notify user that while submitted name exists, it has no debt records to pay for; therefore, debt data must be submitted first before submitting payment data
            toast_message = "<img src='/static/fail-octagon.svg' class='icon fail-icon'><h3>EXISTING NAME WITH NO DEBT RECORDS DETECTED - SUBMIT DEBT DATA FIRST BEFORE ADDING PAYMENT DATA</h3>"

        elif balance_data is not None:
            # use created cursor to add new data into tb_payment_records table
            c.execute('INSERT INTO tb_payment_records(debtor_id, payment_date, principal_paid, interest_paid, total_payment) VALUES(%s, %s, %s, %s, %s)', (debtor_id, pay_date, pay_principal, pay_interest, pay_total, ))

            # update running balance by subtracting pay_total and running_balance
            new_balance = int(balance_data[1]) - int(pay_total)
            
            # use created cursor to update name's existing record from tb_balance_records table
            c.execute('UPDATE tb_balance_records SET running_balance = %s WHERE id = %s', (new_balance, balance_data[0]))

            # store a toast type in a variable for css styling of the toast message to be displayed
            toast_type = 'success'

            # store a toast message in a variable to notify user that submitted name and their debt records exists already, and payment data is added successfully
            toast_message = f"<img src='/static/success-circle.svg' class='icon success-icon'><h3>EXISTING NAME AND THEIR DEBT RECORDS DETECTED - PAYMENT DATA ADDED SUCCESSFULLY!</h3><br><h3>EXISTING DEBTOR'S NAME: {pay_name}</h3><br><p>PAYMENT DATE: {pay_date}<br>PRINCIPAL PAID: {pay_principal}<br>INTEREST PAID: {pay_interest}<br>TOTAL PAYMENT: {pay_total}<br>RUNNING BALANCE: {new_balance}</p>"

    # commit changes to the database
    conn.commit()

    # close cursor and connect objects after the process
    c.close()
    conn.close()

    # return results back to payment_processor() function for jsonification
    return toast_type, toast_message