# import dependencies
import pyodbc

# function 1: retrieve user-submitted data from view history
def view_payment_history(hist_name):
    # debug: print message to confirm that this function has been called
    print('DEBUG: FUNCTION view_payment_history CALLED SUCCESSFULLY!')

    # test: sending processed rows of data to html template
    items = [["1", "2023-10-01", "10000", "1000", "11000"], 
             ["2", "2023-11-01", "5000", "500", "5500"],
             ["3", "2023-10-01", "10000", "1000", "11000"],
             ["4", "2023-11-01", "5000", "500", "5500"], 
             ["5", "2023-10-01", "10000", "1000", "11000"], 
             ["6", "2023-11-01", "5000", "500", "5500"],
             ["7", "2023-10-01", "10000", "1000", "11000"], 
             ["8", "2023-11-01", "5000", "500", "5500"],
             ["9", "2023-10-01", "10000", "1000", "11000"], 
             ["10", "2023-11-01", "5000", "500", "5500"],
             ["11", "2023-10-01", "10000", "1000", "11000"], 
             ["12", "2023-11-01", "5000", "500", "5500"],
             ["1", "2023-10-01", "10000", "1000", "11000"], 
             ["2", "2023-11-01", "5000", "500", "5500"],
             ["3", "2023-10-01", "10000", "1000", "11000"],
             ["4", "2023-11-01", "5000", "500", "5500"], 
             ["5", "2023-10-01", "10000", "1000", "11000"], 
             ["6", "2023-11-01", "5000", "500", "5500"],
             ["7", "2023-10-01", "10000", "1000", "11000"], 
             ["8", "2023-11-01", "5000", "500", "5500"],
             ["9", "2023-10-01", "10000", "1000", "11000"], 
             ["10", "2023-11-01", "5000", "500", "5500"],
             ["11", "2023-10-01", "10000", "1000", "11000"], 
             ["12", "2023-11-01", "5000", "500", "5500"],
             ["1", "2023-10-01", "10000", "1000", "11000"], 
             ["2", "2023-11-01", "5000", "500", "5500"],
             ["3", "2023-10-01", "10000", "1000", "11000"],
             ["4", "2023-11-01", "5000", "500", "5500"], 
             ["5", "2023-10-01", "10000", "1000", "11000"], 
             ["6", "2023-11-01", "5000", "500", "5500"],
             ["7", "2023-10-01", "10000", "1000", "11000"], 
             ["8", "2023-11-01", "5000", "500", "5500"],
             ["9", "2023-10-01", "10000", "1000", "11000"], 
             ["10", "2023-11-01", "5000", "500", "5500"],
             ["11", "2023-10-01", "10000", "1000", "11000"], 
             ["12", "2023-11-01", "5000", "500", "5500"]]
    
    return items