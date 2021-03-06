#!/Applications/anaconda/envs/imgPIL/bin
# Python Challenge - 27
# http://www.pythonchallenge.com/pc/hex/speedboat.html
# http://www.pythonchallenge.com/pc/hex/zigzag.gif
# Username: butter; Password: fly
# Keyword: ../ring/bell.html, repeat, switch

'''
Uses Anaconda environment with Pillow for image processing
    - Python 3.7, numpy, and Pillow (PIL)
    - Run `source activate imgPIL`, `python chall_27.py`
'''

import bz2
import keyword
from PIL import Image


def main():
    '''
    Hint: between the tables, picture of rowboat on lake with zigzag drawn on
    did you say gif?
    oh, and this is NOT a repeat of 14 (spiral matrix)
    '''
    with Image.open('./zigzag_chall_27/zigzag.gif') as img:
        w, h = img.size  # (320, 270). Format: GIF; Mode: P (8-bit pixels)
        # print(img.getextrema())  # Pixel range: 0-255
        palette = img.getpalette()[::3]
        # Pallette to data
        data = img.getdata()  # Seq of flattened pixel values
        oddballs = []
        expected = -1
        i_s = []
        for i, p in enumerate(data):
            if expected >= 0 and p != expected:
                oddballs.append(p)
                i_s.append(i)
            expected = palette[p]

        buzz_data = bz2.decompress(bytearray(oddballs))
        # print(buzz_data)

        # Create image with oddball indices
        '''
        new = Image.new('RGB', (w, h))
        new_data = [(0, 0, 0)] * len(data)
        for i in i_s:
            new_data[i] = (255, 0, 0)
        new.putdata(new_data)
        new.save('./zigzag_chall_27/unexpected.jpg')
        '''
        not_kws = []
        for word in (buzz_data.decode('utf-8')).split():
            if word not in not_kws and not keyword.iskeyword(word):
                not_kws.append(word)
        # ['../ring/bell.html', 'repeat', 'exec', 'print', 'switch']

    return 0


if __name__ == '__main__':
    main()
