#!/usr/local/bin/python3
# Python Challenge - 2
# http://www.pythonchallenge.com/pc/def/ocr.html
# Keyword: equality

import string


def main():
    '''
    Hint: recognize the characters. maybe they are in the book,
    but MAYBE they are in the page source.
    Page source text saved in garbage.txt
    '''

    alphabet = string.ascii_letters
    with open('garbage.txt', 'r') as garbage:
        letters = [c for line in garbage.readlines() for c in line
                   if c in alphabet]
        # Long form of nested loops:
        # letters = []
        # for line in garbage.readlines():
        #     for c in line:
        #         if c in alphabet:
        #             letters.append(c)

    print(''.join(letters))
    return 0


if __name__ == '__main__':
    main()
