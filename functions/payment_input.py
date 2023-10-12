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

    # close cursor and connect objects after the process
    c.close()
    conn.close()