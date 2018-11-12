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
        pixels in the maze walls - black pixels in 1st and last rows
        indicate start and end points)
    Shortest path to solve maze
    '''
    img_path = './maze_chall_24/maze.png'
    with Image.open(img_path) as maze:
        w, h = maze.size  # 641, 641
        # Find the entrance and exit coordinates
        for i in range(w):
            if maze.getpixel((i, 0)) == (0, 0, 0, 255):
                start = (i, 0)
                print('Start: {}'.format(start))
            if maze.getpixel((i, h - 1)) == (0, 0, 0, 255):
                end = (i, h - 1)
                print('Exit: {}'.format(end))

        # Shortest path

    return 0


if __name__ == '__main__':
    main()
