import logging


logging.getLogger(__name__).addHandler(logging.NullHandler())

def main():
    logging.basicConfig(filename='ColumnExpansion.log', level=logging.NOTSET)
    logging.info('>> START')
    doSomething()
    logging.info('>> FINISH')
    

def doSomething():
    logging.info('I am in doSomething method.')

if __name__ == '__main__':
    main()

    