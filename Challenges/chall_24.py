#!/Applications/anaconda/envs/imgPIL/bin
# Python Challenge - 24
# http://www.pythonchallenge.com/pc/hex/ambiguity.html
# Username: butter; Password: fly
# Keyword:

'''
Uses Anaconda environment with Pillow for image processing
    - Python 3.7, numpy, and Pillow (PIL)
    - Run `source activate imgPIL`, `python chall_24.py`
'''

from PIL import Image


def main():
    '''
    From top to bottom; (picture is a huge maze with different colored
        pixels in the maze walls)
    '''
    img_path = './maze_chall_24/maze.png'
    with Image.open(img_path) as maze:
        print(maze.histogram())

    return 0


if __name__ == '__main__':
    main()
