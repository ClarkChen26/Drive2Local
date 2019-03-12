import logging
import src.Drive2LocalConfig

global logger


def setupLogger():
    '''
    Sets up the logger functionality

    '''

    logger = logging.getLogger("Drive2Local")

    # Set up logger called Drive2Local
    logger.setLevel(logging.INFO)

    # Create a FileHandler to store all the log statements
    if src.Drive2LocalConfig.log_root:
        fh = logging.FileHandler(src.Drive2LocalConfig.log_root + "backup.log", mode='w')

    elif src.Drive2LocalConfig.backup_root:
        fh = logging.FileHandler(src.Drive2LocalConfig.backup_root + "backup.log", mode='w')

    else:
        fh = logging.FileHandler("./backup.log", mode='w')

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
    logger.info("Drive2Local Log File")

    return logger


# def errorLog(message):
#     '''
#     Logs an error message using the specified logger above.
#     '''
#
#     logger.error(message)
#
# def debugLog(message):
#     '''
#     Logs an debug message using the specified logger above.
#     '''
#
#     logger.debug(message)
#
# def infoLog(message):
#     '''
#     Logs an info message using the specified logger above.
#     '''
#
#     logger.info(message)
