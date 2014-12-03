SMTPserver = 'aspmx.l.google.com'
print '''
        +=======================================+
        |..........  Mail Forge v 1  ...........|
        +---------------------------------------+
        |# Author: Karl Cyberfreak              |
        |                                       |
        |# Date: 02/12/2014                     |
        |# This tool is made for educational    |
        |# purposes only                        |
        |                                       |
        |# I take no responsibilities for the   |
        |  use of this program !                |
        +=======================================+
        |..........  Mail Forge v 1  ...........|
        +---------------------------------------+
'''
print "Note: - This tool can send mails from any address"
print "This tool uses the SMTP protocol"

def read_from_user():
    host = str(raw_input("Enter hostname of smtp server (example:google.com), leave empty to use default: ")).strip()
    if len(host) > 0:
        global SMTPserver
        SMTPserver = getdns(host)
        print 'SMTP server: '+str(SMTPserver)


    sender      = str(raw_input("Enter Sender address: ")).strip()
    destination = str(raw_input("Enter Destination address : ")).strip()
    subject     = str(raw_input("Enter Email subject: ")).strip()
    content     = str(raw_input("Enter Email content: ")).strip()
    return sender, destination, subject, content


# typical values for text_subtype are plain, html, xml
text_subtype = 'plain'

import sys
import os
import re
import dns.resolver

from smtplib import SMTP
from email.MIMEText import MIMEText

def getdns(host):
    answers = dns.resolver.query(host, 'MX')
    for rdata in answers:
        return str(rdata.exchange).strip()


def run():
    try:
        sender, destination, subject, content = 'kkk@gmail.com','karlheinzniebuhr89@gmail.com','testing','message content'
        #sender, destination, subject, content = read_from_user()

        msg = MIMEText(content, text_subtype)
        msg['Subject']= subject
        msg['From']   = sender # some SMTP servers will do this automatically, not all

        conn = SMTP(SMTPserver)
        conn.set_debuglevel(True)
        conn.ehlo()

        try:
            conn.sendmail(sender, destination, msg.as_string())
        finally:
            print('done')
            conn.close()

    except Exception, exc:
        sys.exit( "mail failed; %s" % str(exc) ) # give a error message




if __name__ == '__main__':
    run()