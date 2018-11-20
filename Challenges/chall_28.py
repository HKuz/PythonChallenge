#!/Applications/anaconda/envs/imgPIL/bin
# Python Challenge - 28
# http://www.pythonchallenge.com/pc/ring/bell.html
# http://www.pythonchallenge.com/pc/ring/green.html
# Username: repeat; Password: switch
# Keyword:

'''
Uses Anaconda environment with Pillow for image processing
    - Python 3.7, numpy, and Pillow (PIL)
    - Run `source activate imgPIL`, `python chall_28.py`
'''

from PIL import Image


def main():
    '''
    Hint: many pairs ring-ring, picture of waterfall
    RING-RING-RING say it out loud
    yes! green!
    '''
    with Image.open('./zigzag_chall_27/zigzag.gif') as img:
        w, h = img.size  # (320, 270). Format: GIF; Mode: P (8-bit pixels)
        pass

    return 0


if __name__ == '__main__':
    main()
