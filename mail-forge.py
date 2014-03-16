#! /usr/local/bin/python


SMTPserver = 'alt4.gmail-smtp-in.l.google.com'
sender =     'karlheinzniebuhr89@gmail.com'
destination = ['karlheinzniebuhr89@gmail.com']

USERNAME = "karlheinzniebuhr89@gmail.com"
PASSWORD = "PASSWORD_INTERNET_SERVICE_PROVIDER"

# typical values for text_subtype are plain, html, xml
text_subtype = 'plain'


content="""\
helo
"""

subject="Sent from Python"

import sys
import os
import re

#from smtplib import SMTP_SSL as SMTP       # this invokes the secure SMTP protocol (port 465, uses SSL)
from smtplib import SMTP                  # use this for standard SMTP protocol   (port 25, no encryption)
from email.MIMEText import MIMEText

try:
    msg = MIMEText(content, text_subtype)
    msg['Subject']=       subject
    msg['From']   = sender # some SMTP servers will do this automatically, not all

    conn = SMTP(SMTPserver)
    conn.set_debuglevel(False)

    #conn.login(USERNAME, PASSWORD)
    try:
        conn.sendmail(sender, destination, msg.as_string())
    finally:
        print('done')
        conn.close()

except Exception, exc:
    sys.exit( "mail failed; %s" % str(exc) ) # give a error message