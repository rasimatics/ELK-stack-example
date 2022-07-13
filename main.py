import logging

formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')

def setup_logger(name: str, log_file: str, level, formatter):

    handler = logging.FileHandler(log_file)
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)
    
    return logger


logger = setup_logger('test', r"C:\Users\Rasim\Desktop\Example app\logs\test.log", logging.INFO, formatter)


for i in range(10):
    if i % 3 == 0:
        logger.error("Error message")
    elif i % 2 == 0:
        logger.info("Info message")
    else:
        logger.warning("Warning message")

logger.critical("Critical message")
