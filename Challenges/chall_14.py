#!/urs/local/bin/python3
# Python challenge - 14
# http://www.pythonchallenge.com/pc/return/italy.html

# Uses Anaconda environment with Pillow for image processing

from PIL import Image
import numpy as np


def main():
    '''
    Hint: walk around. remember: 100*100 = (100+99+99+98) + (...
    http://www.pythonchallenge.com/pc/return/wire.png

    '''
    photo_path = './wire.png'
    photo = Image.open(photo_path)
    wire_pixels = np.asarray(photo)
    print(wire_pixels.shape)  # (1, 10000, 3)

    # Creat numpy array to hold pixels
    height, width = 100, 100
    pic_array = np.zeros((height, width, 3), dtype=np.uint8)

    # Copy wire_pixels in spiral order to pic_array
    wire_index = 0
    n = width
    top, bottom = 0, height
    left, right = 0, width
    direction = 0  # 0: right, 1: down, 2: left, 3: up

    while n > 0:
        if direction == 0:  # RIGHT
            # Copying into row from left to right
            pic_array[top, left:right, :] = \
                wire_pixels[0, wire_index:wire_index + n, :]
            wire_index += n
            n -= 1
            top += 1
        elif direction == 1:  # DOWN
            # Copying into right-most column in order
            pic_array[top:bottom, right - 1, :] = \
                wire_pixels[0, wire_index:wire_index + n, :]
            wire_index += n
            right -= 1
        elif direction == 2:  # LEFT
            # Copying into bottom-most row in reverse order
            pic_array[bottom - 1, left:right, :] = \
                wire_pixels[0, wire_index:wire_index + n, :][::-1]
            wire_index += n
            n -= 1
            bottom -= 1
        elif direction == 3:  # UP
            # Copying into left-most column in reverse order
            pic_array[top:bottom, left, :] = \
                wire_pixels[0, wire_index:wire_index + n, :][::-1]
            wire_index += n
            left += 1

        direction = (direction + 1) % 4

    # Create image from array
    spiral_photo = Image.fromarray(pic_array, "RGB")
    spiral_photo.save('spiral.png')

    return 0

# Keyword: cat


if __name__ == '__main__':
    main()
