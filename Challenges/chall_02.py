#!/usr/local/bin/python3
# Python Challenge - 2
# http://www.pythonchallenge.com/pc/def/ocr.html
# Keyword: equality


def main():
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    letters = []
    with open('garbage.txt', 'r') as garbage:
        for line in garbage.readlines():
            for c in line:
                if c in alphabet:
                    letters.append(c)

    print(''.join(letters))
    return 0


if __name__ == '__main__':
    main()
