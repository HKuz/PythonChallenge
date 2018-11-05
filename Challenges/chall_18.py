#!/usr/local/bin/python3
# Python Challenge - 18
# http://www.pythonchallenge.com/pc/return/balloons.html
# http://www.pythonchallenge.com/pc/return/brightness.html
# http://www.pythonchallenge.com/pc/return/deltas.gz
# Username: huge; Password: file
# Keywords: ../hex/bin.html, butter, fly

import difflib


def main():
    '''
    Hint: can you tell the difference? (side by side pics of swans, one's
        darker than the other)
    brightness -> maybe consider deltas.gz
    '''
    a, b = [], []

    with open('./delta_chall_18/deltas', 'rb') as deltas:
        for line in deltas.readlines():
            a.append(line[:53].decode() + '\n')
            b.append(line[56:].decode())

    diff = difflib.ndiff(a, b)
    # print(type(diff))  # generator

    d_minus = open('./delta_chall_18/d_minus.png', 'wb')
    d_plus = open('./delta_chall_18/d_plus.png', 'wb')
    d_same = open('./delta_chall_18/d_same.png', 'wb')

    for line in diff:
        # Convert non-+/- diff part to byte array
        byte_line = bytes([
            int(n, 16) for n in line[2:].strip().split(" ") if n])
        if line[0] == '+':
            d_plus.write(byte_line)
        elif line[0] == '-':
            d_minus.write(byte_line)
        else:
            d_same.write(byte_line)

    d_minus.close()
    d_plus.close()
    d_same.close()

    return 0


if __name__ == '__main__':
    main()
