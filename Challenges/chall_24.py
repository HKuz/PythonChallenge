#!/Applications/anaconda/envs/imgPIL/bin
# Python Challenge - 24
# http://www.pythonchallenge.com/pc/hex/ambiguity.html
# Username: butter; Password: fly
# Keyword: lake, speed

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
                start = (i, 0)  # (630, 0)
                print('Start: {}'.format(start))
            if maze.getpixel((i, h - 1)) == (0, 0, 0, 255):
                end = (i, h - 1)  # (1, 640)
                # print('Exit: {}'.format(end))

        # Breadth-first shortest path
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # (dw, dh)
        path_queue = [[start]]
        while path_queue:
            # Get and remove oldest path in queue
            tmp_path = path_queue.pop(0)
            # print('Testing path: {}'.format(tmp_path))
            last_pixel = tmp_path[-1]
            if last_pixel == end:
                shortest = tmp_path
                print('Found shortest path')
                break
            for d in directions:
                next_pixel = (last_pixel[0] + d[0], last_pixel[1] + d[1])
                if ((next_pixel not in tmp_path) and
                        (0 <= next_pixel[0] < w) and
                        (0 <= next_pixel[1] < h) and
                        (maze.getpixel(next_pixel) != (255, 255, 255, 255))):
                    # Pixel not already in tmp_path/is in grid/not white
                    # print('Adding next_pixel: {}'.format(next_pixel))
                    new_path = tmp_path + [next_pixel]
                    path_queue.append(new_path)

        r_data = []
        img = Image.new('RGB', (w, h), color=(255, 255, 255))

        for pixel in shortest:
            r_data.append(maze.getpixel(pixel)[0])
            img.putpixel(pixel, maze.getpixel(pixel))

        img.save('./maze_chall_24/path_TMP.jpg')

        with open('./maze_chall_24/maze_tmp.zip', 'wb') as result:
            result.write(bytes(r_data[1::2]))

    return 0


if __name__ == '__main__':
    main()
