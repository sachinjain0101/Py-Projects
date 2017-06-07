from core.main import ColSizeExp
from core.essentials import getAppLogger

if __name__ == '__main__':
    logger = getAppLogger(__name__)
    logger.info('START')
    colsizeexp = ColSizeExp()
    lst = colsizeexp.fmtDict( colsizeexp.calcLinReg())
    logger.info('\n'+str(lst))