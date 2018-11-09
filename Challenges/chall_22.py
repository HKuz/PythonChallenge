#!/usr/local/bin/python3
# Python Challenge - 22
# http://www.pythonchallenge.com/pc/hex/copper.html
# http://www.pythonchallenge.com/pc/hex/white.gif
# Username: butter; Password: fly
# Keyword:

'''
Uses Anaconda environment with Pillow for image processing
    - Python 3.7, numpy, and Pillow (PIL)
    - Run `source activate imgPIL`, `python chall_22.py`
'''

from PIL import Image, ImageDraw


def main():
    '''
    Hint: emulate (picture of joystick)
    <!-- or maybe white.gif would be more bright -->
    http://www.pythonchallenge.com/pc/hex/white.gif shows a 200x200 black
        square, download has 133 pages in preview (frames?)
    '''
    img_path = './joystick_chall_22/white.gif'

    with Image.open(img_path) as gif:
        hist = gif.histogram()  # 1 pixel in hist bin 8 (0-255)
        print(hist.index(1))
        data = list(gif.getdata())
        print(data.index(8))  # 20100

    return 0


if __name__ == '__main__':
    main()
