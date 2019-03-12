import logging
#import Drive2LocalConfig

global logger


def setupLogger(config_list):
    '''
    Sets up the logger functionality

    '''

    logger = logging.getLogger("Drive2Local")

    # Set up logger called Drive2Local
    logger.setLevel(logging.INFO)

    # Create a FileHandler to store all the log statements
    if config_list[9]:
        # Drive2LocalConfig.log_root
        fh = logging.FileHandler(config_list[9] + "backup.log", mode='w')

    elif config_list[8]:
        # Drive2LocalConfig.backup_root
        fh = logging.FileHandler(config_list[8] + "backup.log", mode='w')

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

