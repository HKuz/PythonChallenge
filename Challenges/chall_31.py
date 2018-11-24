#!/usr/local/bin/python3
# Python Challenge - 31
# http://www.pythonchallenge.com/pc/ring/grandpa.html
# http://www.pythonchallenge.com/pc/rock/grandpa.html
# Username: repeat; Password: switch
# Keyword: kohsamui, thailand;

'''
Uses Anaconda environment with Pillow for image processing
    - Python 3.7, numpy, and Pillow (PIL)
    - Run `source activate imgPIL`, `python chall_31.py`
'''

from PIL import Image


def main():
    '''
    Hint: where am I? Picture of rock near a beach
    short break, this ***REALLY*** has nothing to do with Python
    Login required: island: country -> search for Grandpa rock
    Next page:
    UFO's ?
    That was too easy. You are still on 31...
    Window element with iterations attribute of 128
    '''
    left = 0.34
    top = 0.57
    w_step = 0.036  # x-axis = reals
    h_step = 0.027  # y-axis = imaginaries
    max_iter = 128

    with Image.open('./mandelbrot_chall_31/mandelbrot.gif') as mandelbrot:
        w, h = mandelbrot.size
        print('W: {}, H: {}'.format(w, h))

        # f_c(z) = z^2 + c for f_c(0), f_c(f_c(0)), etc.
        for n_iter in range(max_iter):
            pass

    return 0


if __name__ == '__main__':
    main()
