#!/usr/local/bin/python3
# Python Challenge - 21
# ./invader_chall_20/message.zip
# Zip Password: redavni
# Keyword: copper

import zlib
import bz2


def main():
    '''
    Yes! This is really level 21 in here.
    And yes, After you solve it, you'll be in level 22!

    Now for the level:

    * We used to play this game when we were kids
    * When I had no idea what to do, I looked backwards.
    '''

    with open('./invader_chall_20/message/package.pack', 'rb') as z:
        data = z.read()

    z_counter = 0
    b_counter = 0
    r_counter = 0
    log = []

    while True:
        if data.startswith(b'x\x9c'):
            data = zlib.decompress(data)
            z_counter += 1
            log.append(' ')
        elif data.startswith(b'BZh91A'):
            data = bz2.decompress(data)
            b_counter += 1
            log.append('X')
        elif data.endswith(b'\x9cx'):
            data = data[::-1]
            r_counter += 1
            log.append('\n')
        else:
            break

    # data = b'sgol ruoy ta kool'
    # print('Zlib: {}'.format(z_counter))  # 432
    # print('BZ2: {}'.format(b_counter))  # 300
    # print('Reversed: {}'.format(r_counter))  # 9
    print(data.decode()[::-1])  # look at your logs
    print(''.join(log))  # copper

    return 0


if __name__ == '__main__':
    main()
