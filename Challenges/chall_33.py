#!/Applications/anaconda/envs/imgPIL/bin
# Python Challenge - 33
# http://www.pythonchallenge.com/pc/rock/beer.html
# http://www.pythonchallenge.com/pc/rock/beer2.png
# Username: kohsamui; Password: thailand
# Keyword:

'''
Uses Anaconda environment with Pillow for image processing
    - Python 3.7, numpy, and Pillow (PIL)
    - Run `source activate imgPIL`, `python chall_33.py`
'''

import math
from PIL import Image


def main():
    '''
    Hint: 33 bottles of beer on the wall
    If you are blinded by the light,
        remove its power, with its might.
        Then from the ashes, fair and square,
        another truth at you will glare.
    Image is beer1.jpg -> beer2.jpg says "no, png"
    New page is X on black and white
    '''
    path = './light_chall_33/beer2.png'
    with Image.open(path) as beer:
        w, h = beer.size  # 138, 138; mode: L; format: PNG
        histo = beer.histogram()
        # print(histo)

        # Find pixel value for perfect squares in histogram pixel counts
        squares = [(i, n) for i, n in enumerate(histo) if
                   math.sqrt(n).is_integer() and n > 0]
        # [(25, 144), (50, 225), (152, 324)]

        # Remove the brightest of these -> so 324 pixels at value 152
        pix_val, count = squares[-1]
        next_img = Image.new('L', (w, h))
        new_pixels = [p if p != pix_val else 0 for p in beer.getdata()]
        next_img.putdata(new_pixels)
        next_img.save('./light_chall_33/next_img.png')

    return 0


if __name__ == '__main__':
    main()
