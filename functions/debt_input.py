# import dependencies
import psycopg2
import pandas as pd

# function 1: retrieve user-submitted data from debt input
def debt_input(tableName):
    # debug: print message to confirm that this function has been called
    print('DEBUG: FUNCTION debt_input CALLED SUCCESSFULLY!')

    # store localhost, port, database, user, and password details in their respective variables
    host = 'localhost'
    port = '5432'
    database = 'loan_system_db'
    user = 'postgres'
    password = 'valFr3d2020'

    # use psycopg2.connect() function to connect to stated PostgreSQL server
    conn = psycopg2.connect(host = host, port = port, database = database, user = user, password = password)

    # use conn.cursor() function to create a cursor for SQL command execution
    c = conn.cursor()

    # test: save passed table name to variable
    table = tableName

    # test: modifiable SQL code for table query
    tableQuery = "SELECT * FROM " + table

    # test: use created cursor to execute stated SQL code
    c.execute(tableQuery)

    # test: fetch all data gathered by the cursor
    tableData = c.fetchall()

    # test: use pd.dataframe() function to store fetched data into a dataframe
    testDf = pd.DataFrame(tableData, columns = ['id', 'name', 'age', 'address', 'phone_number'])

    # test: return dataframe
    return testDf

    # test: store a print command in a variable, then return it
    # result = print('SUBMITTED:\nName: ', debt_name, '\nDate: ', debt_date, '\nAmount: ', debt_amount, '\nPercent: ', debt_percent, '\nInterest: ', debt_interest, '\nTotal: ', debt_total)

    # return result

resultDb = debt_input('tb_debtor_records')

print(resultDb)