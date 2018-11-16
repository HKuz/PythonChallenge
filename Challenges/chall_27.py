#!/Applications/anaconda/envs/imgPIL/bin
# Python Challenge - 27
# http://www.pythonchallenge.com/pc/hex/speedboat.html
# Username: butter; Password: fly
# Keyword:

'''
Uses Anaconda environment with Pillow for image processing
    - Python 3.7, numpy, and Pillow (PIL)
    - Run `source activate imgPIL`, `python chall_27.py`
'''

from PIL import Image


def main():
    '''
    Hint: between the tables, picture of rowboat on lake with zigzag drawn on
    did you say gif?
    oh, and this is NOT a repeat of 14 (spiral matrix)
    '''
    w, h = 640, 480
    img = Image.new('RGB', (w, h), color=(255, 255, 255))

    img.save('./zigzag_chall_27/final.jpg')

    return 0


if __name__ == '__main__':
    main()
