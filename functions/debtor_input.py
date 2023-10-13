# import dependencies
import psycopg2
import pandas as pd

# import user-created dependencies
from .config import config

# function 1: retrieve user-submitted data from debtor input
def debtor_input(debtor_name, debtor_age, debtor_address, debtor_phone):
    # debug: print message to confirm that this function has been called
    print('DEBUG: FUNCTION debtor_input CALLED SUCCESSFULLY!')

    # call config() function and store results in a variable
    params = config()

    # use psycopg2.connect() function to connect to stated PostgreSQL server
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
        print('NEW DATA ADDED INTO DEBTOR RECORDS SUCCESSFULLY!')

    elif debtor_id is not None:
        # use created cursor to update name's existing record from tb_debtor_records table
        c.execute('UPDATE tb_debtor_records SET age = %s, address = %s, phone_number = %s WHERE id = %s', (debtor_age, debtor_address, debtor_phone, debtor_id, ))
        print('NAME EXISTS IN DEBTOR RECORDS AND ITS RECORD UPDATED SUCCESSFULLY!')

    # commit changes to the database
    conn.commit()

    # use pd.dataframe() function to store fetched data into a dataframe
    #debtorDf = pd.DataFrame(debtorData, columns = ['id', 'name', 'age', 'address', 'phone_number'])

    # close cursor and connect objects after the process
    c.close()
    conn.close()