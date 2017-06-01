#!/Applications/anaconda/envs/pyEffy/bin
# Python challenge - 11
# http://www.pythonchallenge.com/pc/return/5808.html

# Uses Anaconda environment with Pillow for image processing

import PIL, PIL.Image
import numpy as np


def main():
    '''
    Hint: odd even
    '''


    photo_path = './cave.jpg'
    photo = PIL.Image.open(photo_path)
    width = photo.size[0]
    height = photo.size[1]



    # photo.save('cave_final.jpg')

    return 0

# Keyword:


if __name__ == '__main__':
    main()
