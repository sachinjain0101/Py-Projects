from core.main import ColSizeExp
from core.essentials import getAppLogger, Vars
import smtplib
import time

logger = None

def sendMail(body):
    try:
        server = smtplib.SMTP(Vars.SMTP_ADDR)
        server.ehlo()
        server.starttls()
        server.login(Vars.SMTP_USER, Vars.SMTP_PWD)
        currTime=time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime())
        server.sendmail(Vars.EMAIL_FROM, Vars.EMAIL_TO, Vars.MESSAGE.format(Vars.EMAIL_FROM,Vars.EMAIL_TO,currTime,body))
        server.close()
        logger.info( 'successfully sent the mail')
    except:
        logger.info( 'failed to send mail')

if __name__ == '__main__':
    logger = getAppLogger(__name__)
    logger.info('START')
    colsizeexp = ColSizeExp()
    body=colsizeexp.getHTMLOutput()
    sendMail(body)
    logger.info('DONE')
