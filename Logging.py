import logging
import config

# Set up logger called Drive2Local
logger = logging.getLogger("Drive2Local")
logger.setLevel(logging.INFO)

# Create a FileHandler to store all the log statements
fh = logging.FileHandler(config.backup_root + 'Drive2Local.log', mode='w')

# Create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(message)s')
fh.setFormatter(formatter)

# Create a StreamHandler to output the logs to the console
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
ch.setFormatter(formatter)

# Add the handlers to the logger
logger.addHandler(fh)
logger.addHandler(ch)

def errorLog(message):
    '''
    Logs an error message using the specified logger above.
    '''

    logger.error(message)

def debugLog(message):
    '''
    Logs an debug message using the specified logger above.
    '''

    logger.debug(message)

def infoLog(message):
    '''
    Logs an info message using the specified logger above.
    '''

    logger.info(message)
