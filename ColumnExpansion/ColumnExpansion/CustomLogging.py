import logging

class CustomLogging(object):
    """CustomeLogging handles logging of all modules of this project"""

    def __init__(self):
        pass
        
    def log(self,msg, path='colexp-baselog.log', multipleLocs=True):
        fmt_str = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        formatter = logging.Formatter(fmt_str)
        logging.basicConfig(filename=path, level=logging.NOTSET, format=fmt_str)
 
        if multipleLocs:
            console = logging.StreamHandler()
            console.setLevel(logging.NOTSET)
            console.setFormatter(formatter)
            logging.getLogger("").addHandler(console)

        logging.info(msg)


