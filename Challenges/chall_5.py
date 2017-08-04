#!/urs/local/bin/python3
# Python challenge - 5
# http://www.pythonchallenge.com/pc/def/peak.html

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
        print(data)

        for row in data:
            # Rows of lists, add to 95 with characters to print
            print(''.join([r[0] * r[1] for r in row]))

    return 0

# Keyword: channel


if __name__ == '__main__':
    main()
