#!/usr/local/bin/python3
# Python Challenge - 24
# http://www.pythonchallenge.com/pc/hex/ambiguity.html
# Username: butter; Password: fly
# Keyword:

import urllib.request
import urllib.parse
import codecs


def main():
    '''

    '''
    # From level 17
    violin_url = 'http://www.pythonchallenge.com/pc/stuff/violin.php'
    message = codecs.decode('sorry', 'rot-13')
    print(message)
    # sorry in German: 'Es tut uns leid'
    quoted = urllib.parse.quote_plus(message)
    request = urllib.request.Request(
        violin_url, headers={'Cookie': 'info=' + quoted}
    )
    response = urllib.request.urlopen(request).read().decode()
    print(response)  # didn't work

    return 0


if __name__ == '__main__':
    main()
