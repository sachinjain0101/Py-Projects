
import smtplib
import os
import Vars
import sys

message = '\r\n'.join(['From: {0}',
          'To: {1}',
          'MIME-Version: 1.0',
          'Content-type: text/html',
          'Subject: Second HTML message',
          '',
          '{2}'])

body="""
        <!DOCTYPE html>
        <html>
        <body>

        <h1>My First Heading</h1>

        <p>My first paragraph.</p>

        </body>
        </html>
     """

try:
    server = smtplib.SMTP(Vars.SMTP_ADDR)
    server.ehlo()
    server.starttls()
    server.login(Vars.SMTP_USER, Vars.SMTP_PWD)
    server.sendmail(Vars.EMAIL_FROM, Vars.EMAIL_TO, message.format(Vars.EMAIL_FROM,Vars.EMAIL_TO,body))
    server.close()
    print 'successfully sent the mail'
except:
    print 'failed to send mail'

#sys.exit(0)