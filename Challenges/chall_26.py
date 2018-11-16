#!/usr/local/bin/python3
# Python Challenge - 26
# http://www.pythonchallenge.com/pc/hex/decent.html
# Username: butter; Password: fly
# Keyword: speedboat

import smtplib
from email.message import EmailMessage
import hashlib


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

        # Open a plain text file with message content to read
        with open(textfile) as fp:
            msg = EmailMessage()
            msg.set_content(fp.read())

        msg['Subject'] = 'The contents of %s' % textfile
        msg['From'] = hk
        msg['To'] = leo

        # Send the message via an SMTP server
        s = smtplib.SMTP('smtp.gmail.com', '587')
        s.ehlo()
        s.starttls()
        s.login(hk, pw)
        s.send_message(msg)
        s.quit()

    # Response
    '''
    ------------
    Never mind that.

    Have you found my broken zip?

    md5: bbb8b499a0eef99b52c7f13f4e78c24b

    Can you believe what one mistake can lead to?
    ------------

    MD5 algorithm: a hash function producing a 128-bit hash value. Although
        MD5 was initially designed to be used as a cryptographic hash
        function, it has been found to suffer from extensive vulnerabilities.
        It can still be used as a checksum to verify data integrity, but only
        against unintentional corruption (Wikipedia)

    Zip from challenge 25 had a broken zip in it, but opened okay
    Picture of the word "speed"
    '''
    md5 = 'bbb8b499a0eef99b52c7f13f4e78c24b'
    found = False
    with open('./maze_chall_24/maze/mybroken.zip', 'rb') as maze_zip:
        broken = maze_zip.read()
        for datum in range(len(broken)):
            for byte in range(256):
                fixed = broken[:datum] + bytes([byte]) + broken[datum + 1:]
                if hashlib.md5(fixed).hexdigest() == md5:
                    with open('./email_chall_26/fixed.zip', 'wb') as f:
                        f.write(fixed)
                        found = True
                        break
            if found:
                break

    return 0


if __name__ == '__main__':
    main()
