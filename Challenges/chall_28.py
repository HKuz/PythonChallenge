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
    with Image.open('./ring_chall_28/bell.png') as bell:
        w, h = bell.size  # (640, 480). Format: PNG; Mode: RGB
        pass

    return 0


if __name__ == '__main__':
    main()
