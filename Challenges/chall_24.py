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
        pixels along the path - black pixels in 1st and last rows
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

        # Breadth-first shortest path
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # (dw, dh)
        data = []
        path_queue = [start]
        while len(path_queue) != 0:
            # Get and remove oldest element in pathQueue
            tmp_path = path_queue.pop(0)
            last_pixel = tmp_path[-1]
            if last_pixel == end:
                shortest = tmp_path
                break
            for dw, dh in directions:
                next_pixel = (last_pixel[0] + dw, last_pixel[1] + dh)
                if not ((0 <= next_pixel[0] < w) and (0 <= next_pixel[1] < h)):
                    # Off grid, check next direction
                    continue
                elif ((next_pixel not in tmp_path) and
                      maze.getpixel(next_pixel) != (255, 255, 255, 255)):
                    # Pixel isn't already in the path and it's not white
                    new_path = tmp_path + [next_pixel]
                    path_queue.append(new_path)
            # for nextNode in graph.childrenOf(lastNode):
            #     if nextNode not in tmpPath:
            #         newPath = tmpPath + [nextNode]
            #         pathQueue.append(newPath)

        for pixel in shortest:
            data.append(maze.getpixel(pixel)[0])

        print(data)

    return 0


if __name__ == '__main__':
    main()
