# import dependencies
from configparser import ConfigParser

# define a function for config parsing process
def config(filename = 'database.ini', section = 'postgresql'):
    # debug: print message to confirm that this function has been called
    print('DEBUG: FUNCTION config CALLED SUCCESSFULLY!')

    # create a parser object
    parser = ConfigParser()

    # use parser object to read config file
    parser.read(filename)

    # create an empty dictionary to store config file data later
    db = {}

    # if-statement to confirm a section exists in config file prior to processing
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