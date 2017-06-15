
import smtplib
import os
import Vars
import sys

message = '\r\n'.join(['From: {0}',
          'To: {1}',
          'Subject: Just another message',
          '',
          'Why, oh why'])

try:
    server = smtplib.SMTP(Vars.SMTP_ADDR)
    server.ehlo()
    server.starttls()
    server.login(Vars.SMTP_USER, Vars.SMTP_PWD)
    server.sendmail(Vars.EMAIL_FROM, Vars.EMAIL_TO, message.format(Vars.EMAIL_FROM,Vars.EMAIL_TO))
    server.close()
    print 'successfully sent the mail'
except:
    print 'failed to send mail'

sys.exit(0)