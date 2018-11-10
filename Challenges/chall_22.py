#!/usr/local/bin/python3
# Python Challenge - 22
# http://www.pythonchallenge.com/pc/hex/copper.html
# http://www.pythonchallenge.com/pc/hex/white.gif
# Username: butter; Password: fly
# Keyword: bonus

'''
Uses Anaconda environment with Pillow for image processing
    - Python 3.7, numpy, and Pillow (PIL)
    - Run `source activate imgPIL`, `python chall_22.py`
'''

from PIL import Image, ImageDraw


def main():
    '''
    Hint: emulate (picture of joystick)
    <!-- or maybe white.gif would be more bright -->
    http://www.pythonchallenge.com/pc/hex/white.gif shows a 200x200 black
        square, download has 133 pages in preview (frames?)
    '''
    img_path = './joystick_chall_22/white.gif'

    with Image.open(img_path) as gif:
        # print('Format: {}, Mode: {}'.format(gif.format, gif.mode))  # GIF, P
        indices = []
        while True:
            hist = gif.histogram()  # 1 pixel in hist bin 8 (0-255)
            color = hist.index(1)  # bin 8 out of 256
            # print('Color bin: {}'.format(color))
            data = list(gif.getdata())
            pixel_index = data.index(color)  # 20100 in 1st frame
            indices.append(pixel_index)
            # print('Pixel index: {}'.format(pixel_index))

            try:
                # Note: gif.n_frames gives total frames (133)
                gif.seek(gif.tell() + 1)
                # print('Frame: {}'.format(gif.tell() + 1))
            except EOFError:
                break  # end of sequence

        # Convert flattened indices to get position on 200x200 square
        coords = list(map(lambda x: divmod(x, 200), indices))
        # print(sum([1 for r, c in coords if r == 100 == c]))  # 5

        new = Image.new('RGB', (500, 200))
        draw = ImageDraw.Draw(new)
        x, y = (0, 100)
        for coord in coords:
            dx = coord[1] - 100
            dy = coord[0] - 100
            if coord == (100, 100):
                # New letter, move right and reset height
                x += 50
                y = 100
            x += dx
            y += dy
            draw.point((x, y))

        new.save('./joystick_chall_22/final.jpg')

    return 0


if __name__ == '__main__':
    main()
