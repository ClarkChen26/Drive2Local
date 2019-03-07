import logging
import config

logger = logging.getLogger("Drive2Local")
logger.setLevel(logging.INFO)
fh = logging.FileHandler(config.backup_root + 'Drive2Local.log', mode='w')

# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(message)s')
fh.setFormatter(formatter)
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
ch.setFormatter(formatter)
# add the handlers to the logger
logger.addHandler(fh)
logger.addHandler(ch)

def errorLog(message):
    logger.error(message)

def debugLog(message):
    logger.debug(message)

def infoLog(message):
    logger.info(message)
