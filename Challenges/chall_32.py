#!/usr/local/bin/python3
# Python Challenge - 32
# http://www.pythonchallenge.com/pc/rock/arecibo.html
# http://www.pythonchallenge.com/pc/rock/warmup.txt
# http://www.pythonchallenge.com/pc/rock/up.html
# http://www.pythonchallenge.com/pc/rock/up.txt
# Username: kohsamui; Password: thailand
# Keyword: up,


def main():
    '''
    Hint: etch-a-sketch
    fill in the blanks
    for warmup.txt -> dimensions and parameters for a 9x9 challenge
    Solve that, see arrow pointing up
    up.html -> 32 x 32 challenge
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

    rows = 0
    cols = 0
    horiz = []
    vert = []
    board = [[None] * self.cols] * self.rows

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

                # Line isn't newline or comment (contains numbers)
                nums = tuple([int(n) for n in line.split(' ')])
                if d_flag:
                    self.rows, self.cols = nums

                elif h_flag:
                    self.horiz.append(nums)

                elif v_flag:
                    self.vert.append(nums)

            print('Dimensions: {} x {}'.format(self.dim_x, self.dim_y))
            print('Horizontals:')
            for h in self.horiz:
                print(h)
            print('Verticals:')
            for v in self.vert:
                print(v)

        def show_board(self):
            pass


if __name__ == '__main__':
    main()
