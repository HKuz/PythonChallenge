#!/usr/local/bin/python3
# Python Challenge - 26
# http://www.pythonchallenge.com/pc/hex/decent.html
# Username: butter; Password: fly
# Keyword: speedboat

import smtplib
from email.message import EmailMessage


def main():
    '''
    Hint: be a man - apologize!
    Picture of monkeys, underneath: Hurry up, I'm missing the boat
    you've got his email
    '''
    send_email = False

    if send_email:
        leo = 'leopold.moz@pythonchallenge.com'
        hk = 'hkuzdev@gmail.com'
        pw = input('Email password:')
        textfile = './email_chall_26/msg.txt'

        # Open a plain text file for reading.  For this example, assume that
        # the text file contains only ASCII characters.
        with open(textfile) as fp:
            msg = EmailMessage()
            msg.set_content(fp.read())

        msg['Subject'] = 'The contents of %s' % textfile
        msg['From'] = hk
        msg['To'] = leo

        # Send the message via our own SMTP server, but don't include the
        # envelope header.
        s = smtplib.SMTP('smtp.gmail.com', '587')
        s.ehlo()
        s.starttls()
        s.login(hk, pw)
        # s.sendmail(hk, [leo], msg.as_string())
        s.send_message(msg)
        s.quit()

    # Response
    '''
    Never mind that.

    Have you found my broken zip?

    md5: bbb8b499a0eef99b52c7f13f4e78c24b

    Can you believe what one mistake can lead to?
    '''

    return 0


if __name__ == '__main__':
    main()
