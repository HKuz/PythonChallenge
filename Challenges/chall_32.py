#!/usr/local/bin/python3
# Python Challenge - 32
# http://www.pythonchallenge.com/pc/rock/arecibo.html
# Username: kohsamui; Password: thailand
# Keyword:

import re


def main():
    '''
    Hint: etch-a-sketch
    fill in the blanks
    for warmup.txt
    '''
    warmup_path = './etchasketch_chall_32/warmup.txt'
    EtchASketch(warmup_path)
    return 0


class EtchASketch(object):
    """
    Takes a filepath to a text file containing the parameters of the board.
        Board must have x by y dimensions on one line, separated by a space
        Horizontal params one per line, each number separated by a space
        Vertical params one per line, each number separated by a space
        Finds a solution where tiles are filled and grouped per h and v params
    """

    dim_x = 0
    dim_y = 0
    horiz = []
    vert = []

    def __init__(self, path):
        self.path = path
        self.get_params(path)

    def get_params(self, path):
        with open(path, 'r') as params:
            for line in params.readlines():
                if line.startswith('\n'):
                    continue
                if line.startswith('# Dimensions'):
                    d_flag, h_flag, v_flag = True, False, False
                    continue
                elif line.startswith('# Horizontal'):
                    d_flag, h_flag, v_flag = False, True, False
                    continue
                elif line.startswith('# Vertical'):
                    d_flag, h_flag, v_flag = False, False, True
                    continue

                if d_flag:
                    pass

                elif h_flag:
                    pass

                elif v_flag:
                    pass

            print('Dimensions: {} x {}'.format(self.dim_x, self.dim_y))
            print('Horizontals:')
            for h in self.horiz:
                print(h)
            for v in self.vert:
                print(v)


if __name__ == '__main__':
    main()
