""" Set up logging"""
import logging
import logging.handlers
import os

LOGGERS = {}


def init(name):
    """ Set up logging """

    if LOGGERS.get(name):
        return LOGGERS[name]

    log_dir = 'logs'
    os.makedirs(log_dir, exist_ok=True)

    log_filename = f"{log_dir}/{name}.log"
    LOGGERS[name] = logging.getLogger(name)
    LOGGERS[name].setLevel(logging.INFO)

    handler = logging.handlers.TimedRotatingFileHandler(log_filename, when='midnight', backupCount=365)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    LOGGERS[name].addHandler(handler)

    return LOGGERS[name]
