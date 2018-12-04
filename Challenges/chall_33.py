#!/Applications/anaconda/envs/imgPIL/bin
# Python Challenge - 33
# http://www.pythonchallenge.com/pc/rock/beer.html
# http://www.pythonchallenge.com/pc/rock/beer2.png
# Username: kohsamui; Password: thailand
# Keyword: gremlins

'''
Uses Anaconda environment with Pillow for image processing
    - Python 3.7, numpy, and Pillow (PIL)
    - Run `source activate imgPIL`, `python chall_33.py`
'''

import math
import numpy as np
from PIL import Image


def main():
    '''
    Hint: 33 bottles of beer on the wall
    If you are blinded by the light,
        remove its power, with its might.
        Then from the ashes, fair and square,
        another truth at you will glare.
    Image is beer1.jpg -> beer2.jpg says "no, png"
    New page has greyscale image
    '''
    path = './light_chall_33/beer2.png'
    with Image.open(path) as beer:
        w, h = beer.size  # 138, 138; mode: L; format: PNG
        mode = beer.mode
        histo = np.array([(pix, count) for pix, count in
                          enumerate(beer.histogram()) if count != 0])
        # print(histo)  # Length is 66, pixels come in consecutive pairs

        # Find where pixel counts still make a square -> every other index
        # sqrts = [np.sqrt(p) for p in np.cumsum(histo[:, 1])]
        # print(sqrts)

        data = list(beer.getdata())
        for i in range(len(histo) - 2, 0, -2):
            # Start at index 64, jump back by 2's, remove 2 brightest pixels,
            #   reshape image, save as new image
            data = [x for x in data if x < histo[i][0]]
            side = int(math.sqrt(len(data)))
            next_img = Image.new(mode, (side, side))
            next_img.putdata(data)
            next_img.save('./light_chall_33/res_{}.png'
                          .format(int((64 - i) / 2)))

        # Result:
        # xxxxxxxxxxxvrnegarwinemoldinosl_
        # 'Squared' letters: gremlins

    return 0


if __name__ == '__main__':
    main()
