#!/usr/local/bin/python3
# Python Challenge - 5
# http://www.pythonchallenge.com/pc/def/peak.html
# Keyword: channel

import urllib.request
import pickle


def main():
    '''
    Hint: pronounce it (image of hill)
    Comment: Peak hell sounds familiar ?
    '''
    banner_url = 'http://www.pythonchallenge.com/pc/def/banner.p'

    with urllib.request.urlopen(banner_url) as banner:
        raw_data = banner.read()
        data = pickle.loads(raw_data)
        # print(data)
        # print('Rows: {}'.format(len(data)))
        for row in data:
            # print(len(row))
            # print(sum([n for s, n in row]))
            # Rows of lists, add to 95 with characters to print
            print(''.join([s * n for s, n in row]))

    return 0


if __name__ == '__main__':
    main()
