#!/usr/local/bin/python3
# Python Challenge - 29
# http://www.pythonchallenge.com/pc/ring/guido.html
# Username: repeat; Password: switch
# Keyword:

import urllib.request


def main():
    '''
    Hint: silence!
    whoisit.jpg
    '''
    url = 'http://www.pythonchallenge.com/pc/ring/guido.html'
    with urllib.request.urlopen() as page:
        print(page.read())

    return 0


if __name__ == '__main__':
    main()
