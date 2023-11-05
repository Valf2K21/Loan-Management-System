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

# create a function to process user-submitted data from debtor input
def debtor_input(debtor_name, debtor_age, debtor_address, debtor_phone):
    # call config() function and store server parameters in a variable
    params = config()

    # use psycopg2.connect() function to connect to PostgreSQL server
    # note: ** means we want to extract the values of the returned dictionary stored in parans variable
    conn = psycopg2.connect(**params)

    # use conn.cursor() function to create a cursor for SQL command execution
    c = conn.cursor()

    # use created cursor to check if user-inputted name is already in the tb_debtor_records table
    c.execute('SELECT id FROM tb_debtor_records WHERE name = %s', (debtor_name, ))

    # fetch data gathered by the cursor
    debtor_id = c.fetchone()

    # if-elif statement to check if the query returned a record that matches debtor_name
    if debtor_id is None:
        # use created cursor to add new data into tb_debtor_records table
        c.execute('INSERT INTO tb_debtor_records(name, age, address, phone_number) VALUES(%s, %s, %s, %s)', (debtor_name, debtor_age, debtor_address, debtor_phone, ))
        
        # store a toast type in a variable for css styling of the toast message to be displayed
        toast_type = 'success'

        # store a toast message in a variable to notify user that submitted name is new and  debtor data is added successfully
        toast_message = f"<img src='/static/success-circle.svg' class='icon success-icon'><h3>NEW NAME DETECTED AND DEBTOR DATA ADDED SUCCESSFULLY!</h3><p>DEBTOR'S NAME: {debtor_name}<br>AGE: {debtor_age}<br>ADDRESS: {debtor_address}<br>PHONE NUMBER: {debtor_phone}</p>"

    elif debtor_id is not None:
        # use created cursor to collect existing data that matches debtor_name
        c.execute('SELECT age, address, phone_number FROM tb_debtor_records WHERE name = %s', (debtor_name, ))

        # fetch data gathered by the cursor
        old_data = c.fetchone()

        # extract returned tuple into their respective variables
        debtor_age_old = old_data[0]
        debtor_address_old = old_data[1]
        debtor_phone_old = old_data[2]

        # use created cursor to update name's existing record from tb_debtor_records table
        c.execute('UPDATE tb_debtor_records SET age = %s, address = %s, phone_number = %s WHERE id = %s', (debtor_age, debtor_address, debtor_phone, debtor_id, ))
        
        # store a toast type in a variable for css styling of the toast message to be displayed
        toast_type = 'alert'

        # store a toast message in a variable to notify user that submitted name exists already and debtor data is updated successfully
        toast_message = f"<img src='/static/alert-triangle.svg' class='icon alert-icon'><h3>EXISTING NAME DETECTED AND DEBTOR DATA UPDATED SUCCESSFULLY!</h3><h3>EXISTING DEBTOR'S NAME: {debtor_name}</h3><h3>OLD DATA:</h3><p>AGE: {debtor_age_old}<br>ADDRESS: {debtor_address_old}<br>PHONE NUMBER: {debtor_phone_old}</p><h3>NEW DATA:</h3><p>AGE: {debtor_age}<br>ADDRESS: {debtor_address}<br>PHONE NUMBER: {debtor_phone}</p>"

    # commit changes to the database
    conn.commit()

    # close cursor and connect objects after the process
    c.close()
    conn.close()

    # return results back to debtor_processor() function for jsonification
    return toast_type, toast_message