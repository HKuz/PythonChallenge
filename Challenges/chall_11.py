#!/Applications/anaconda/envs/imgPIL/bin
# Python Challenge - 11
# http://www.pythonchallenge.com/pc/return/5808.html
# Username: huge; Password: file
# Keyword: evil

'''
Uses Anaconda environment with Pillow for image processing
    - Python 3.7, numpy, and Pillow (PIL)
    - Run `source activate imgPIL`, `python chall_11.py`
'''

from PIL import Image
import numpy as np


def main():
    '''
    Hint: odd even
    '''

    photo_path = './odd-even_chall_11/cave.jpg'
    photo = Image.open(photo_path)
    width, height = photo.size  # 640, 480

    # Load image into numpy array
    pixel_data = np.asarray(photo)
    # pixel_data.shape: 480 rows, 640 pixels/row, 3 points with RGB info
    even_pixels = np.zeros((height, width // 2, 3), dtype=np.uint8)
    odd_pixels = np.zeros((height, width // 2, 3), dtype=np.uint8)

    # Split image into two by even and odd pixels
    for row in range(height):
        even_pixels[row] = (pixel_data[row, ::2, :] if row % 2 == 0
                            else pixel_data[row, 1::2, :])
        odd_pixels[row] = (pixel_data[row, ::2, :] if row % 2 == 1
                           else pixel_data[row, 1::2, :])

    # Draw new images and save
    even_photo = Image.fromarray(even_pixels, "RGB")
    even_photo.save('./odd-even_chall_11/even.jpg')
    odd_photo = Image.fromarray(odd_pixels, "RGB")
    odd_photo.save('./odd-even_chall_11/odd.jpg')

    return 0


if __name__ == '__main__':
    main()
