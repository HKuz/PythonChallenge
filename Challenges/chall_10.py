#!/usr/local/bin/python3
# Python Challenge - 10
# http://www.pythonchallenge.com/pc/return/bull.html
# http://www.pythonchallenge.com/pc/return/sequence.txt
# Username: huge; Password: file
# Keyword: 5808

import re


def main():
    '''
    Hint: len(a[30]) = ?
    a = [1, 11, 21, 1211, 111221,
    <area shape="poly" coords="146, ..., 399" href="sequence.txt">
    '''
    # a_orig = ['1', '11', '21', '1211', '111221']

    # Naive solution
    '''
    a = ['1']
    for i in range(30):
        curr_string = a[i]
        new_string = ''

        prev_char = curr_string[0]
        pos = 1
        count = 1
        while pos < len(curr_string):
            # Check if character same as prior
            # Y: increment count and position
            # N: add to newS and reset
            curr_char = curr_string[pos]
            if curr_char == prev_char:
                # Same num, increment count and position
                count += 1
                pos += 1
            else:
                # Different num; tack count and num to new_string, reset vars
                new_string += str(count) + prev_char
                prev_char = curr_string[pos]
                count = 1
                pos += 1

        # Pick up the last number and its count
        new_string += str(count) + prev_char
        a.append(new_string)

    # print(a)
    # print(a[30])
    print('Length of a[30]: {}'.format(len(a[30])))
    '''

    # Regular Expression solution
    a = '1'
    pattern = re.compile(r'(\d)(\1*)')

    for i in range(30):
        a = ''.join([str(len(times) + 1) + letter for letter, times
                     in re.findall(pattern, a)])

    print('Length of a[30]: {}'.format(len(a)))
    return 0


if __name__ == '__main__':
    main()
