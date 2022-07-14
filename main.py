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


for i in range(100):
    if i % 3 == 0:
        logger.error("Updated Error message")
    elif i % 2 == 0:
        logger.info("Updated Info message")
    else:
        logger.warning("Updated Warning message")

logger.critical("Updated Critical message")


"""

2022/07/01 10:14:27 [error] 

3961730#3961730: *1 FastCGI sent in stderr: "PHP message: PHP Warning:  php_strip_whitespace(): Filename cannot be empty in /home/ubuntu/demo/chats/helperchat/livehelperchat-master/lhc_web/lib/core/lhtpl/tpl.php on line 236" while reading response header from upstream, client: 10.23.33.12, server: , request: "GET /index.php/site_admin/chatbox/new HTTP/1.1", upstream: "fastcgi://unix:/var/run/php/php7.4-fpm.sock:", host: "10.23.19.19:8003", referrer: "http://10.23.19.19:8003/index.php/site_admin/chatbox/list"

"""