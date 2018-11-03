#!/usr/local/bin/python3
# Python Challenge - 4
# http://www.pythonchallenge.com/pc/def/linkedlist.html
# http://www.pythonchallenge.com/pc/def/linkedlist.php
# Keyword: peak

import urllib.request
import re


def main():
    '''
    html page shows: linkedlist.php
    php page comment: urllib may help. DON'T TRY ALL NOTHINGS, since it will
        never end. 400 times is more than enough.
    Photo link: linkedlist.php?nothing=12345
    http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345
    44827
    45439
    ...
    '''
    base_url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
    nothing = '12345'
    # nothing = '66831'  # Cheat code for last nothing
    pattern = re.compile(r'next nothing is (\d+)')

    while True:
        with urllib.request.urlopen(base_url + nothing) as page:
            data = page.read().decode('utf-8')
            # print(data)
            match = re.search(pattern, data)
            if match:
                nothing = match.group(1)
                if nothing == '16044':
                    nothing = str(16044 / 2)
            else:
                print('Hit break')
                break

    print('Last nothing found was: {}'.format(nothing))
    return 0


if __name__ == '__main__':
    main()
