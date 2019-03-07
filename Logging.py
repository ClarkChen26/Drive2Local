import logging
import config

# logging.basicConfig(level=logging.DEBUG,
#                     format='%(asctime)s %(levelname)s %(message)s',
#                     filename=config.backup_root + "Drive2Local.log",
#                     filemode='w')

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(message)s',
                    filename=config.backup_root + "Drive2Local.log",
                    filemode='w')

def errorLog(message):
    logging.error(message)


def debugLog(message):
    logging.debug(message)

def infoLog(message):
    logging.info(message)

# def warnLog(message):
#     logging.warning(message)

