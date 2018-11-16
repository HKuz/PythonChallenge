#!/usr/local/bin/python3
# Python Challenge - 26
# http://www.pythonchallenge.com/pc/hex/decent.html
# Username: butter; Password: fly
# Keyword:

import smtplib
from email.mime.text import MIMEText


def main():
    '''
    Hint: be a man - apologize!
    Picture of monkeys, underneath: Hurry up, I'm missing the boat
    you've got his email
    '''

    leo = 'leopold.moz@pythonchallenge.com'
    hk = 'heather.kusmierz@gmail.com'

    # Open a plain text file for reading.  For this example, assume that
    # the text file contains only ASCII characters.
    msg = MIMEText('sorry')

    # me == the sender's email address
    # you == the recipient's email address
    msg['Subject'] = 'Apology'
    msg['From'] = hk
    msg['To'] = leo

    # Send the message via our own SMTP server, but don't include the
    # envelope header.
    s = smtplib.SMTP('localhost')
    s.sendmail(hk, [leo], msg.as_string())
    s.quit()

    return 0


if __name__ == '__main__':
    main()
