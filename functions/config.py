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
from configparser import ConfigParser

# define a function for config parsing process
def config(filename = 'database.ini', section = 'postgresql'):
    # create a parser object
    parser = ConfigParser()

    # use parser object to read config file
    parser.read(filename)

    # create an empty dictionary to store config file data later
    db = {}

    # if-else statement to confirm if passed section exists in config file prior to processing
    if parser.has_section(section):
        # get the saved parameters in that section
        params = parser.items(section)

        # create a for-loop to loop through the gathered parameters
        for param in params:
            # save the currently iterated key-value pair inside the empty dictionary
            db[param[0]] = param[1]
    
    else:
        # create an exception to notify user that section is not found in config file
        raise Exception('Section {0} is not found in the {1} file.'.format(section, filename))
    
    # return filled dictionary
    return db