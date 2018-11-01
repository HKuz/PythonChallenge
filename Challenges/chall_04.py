#!/urs/local/bin/python3
# Python challenge - 4
# http://www.pythonchallenge.com/pc/def/linkedlist.php

import urllib.request
import re


def main():
    '''
    http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345
    44827
    45439
    ...
    '''
    base_url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
    nothing = '12345'
    # nothing = '66831' # Cheat code
    pattern = re.compile(r'next nothing is (\d+)')

    for i in range(400):
        with urllib.request.urlopen(base_url + nothing) as page:
            data = page.read().decode('utf-8')
            print(data)
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

# Keyword: peak


if __name__ == '__main__':
    main()