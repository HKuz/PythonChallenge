#!/Applications/anaconda/envs/imgPIL/bin
# Python Challenge - 16
# www.pythonchallenge.com/pc/return/mozart.html
# Username: huge; Password: file
# Keyword: romance

'''
Uses Anaconda environment with Pillow for image processing
    - Python 3.7, numpy, and Pillow (PIL)
    - Run `source activate imgPIL`, `python chall_16.py`
'''

from PIL import Image
import numpy as np


def main():
    '''
    Hint: let me get this straight
    Image has bars of 5 pink pixels with two white ones on ends,
        seemingly one/row
    Need to align the pink bars
    '''
    photo_path = './mozart-static_chall_16/mozart.gif'
    photo = Image.open(photo_path)
    width, height = photo.size  # 640, 480
    mode = photo.mode  # P

    # 5th row (index 4), 106th pixel (index 105) is pink
    # print('Pink pixel: {}'.format(photo.getpixel((106, 4)))) # 195
    pink = 195

    photo_array = np.asarray(photo)
    shifted_array = np.zeros((height, width), dtype=np.uint8)

    for y in range(height):
        for x in range(width - 4):
            if photo.getpixel((x, y)) == pink and \
                    photo.getpixel((x + 4, y)) == pink:
                # Number of pixels from pink to end is width - x
                shifted_array[y, 0:width - x] = photo_array[y, x:]
                shifted_array[y, width - x:] = photo_array[y, 0:x]

    # Create new photo from re-aligned rows
    new_img = Image.fromarray(shifted_array, mode)
    new_img.save('./mozart-static_chall_16/mozart_16_solution.gif')

    return 0


if __name__ == '__main__':
    main()
