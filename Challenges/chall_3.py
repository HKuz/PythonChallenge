#!/Applications/anaconda/envs/Python3/bin
# Python challenge - 3
# http://www.pythonchallenge.com/pc/def/equality.html

import re


'''
Hint:
One small letter surrounded by EXACTLY three big bodyguards on each of its sides.
'''


def main():
    with open('bodyguard.txt', 'r') as bodyguard:
        pattern = re.compile(r'[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]')
        littles = ''
        text = bodyguard.read()
        littles = re.findall(pattern, text)

    print(''.join(littles))
    # linkedlist
    return 0


if __name__ == '__main__':
    main()
