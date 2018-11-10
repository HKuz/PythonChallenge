#!/usr/local/bin/python3
# Python Challenge - 22
# http://www.pythonchallenge.com/pc/hex/copper.html
# http://www.pythonchallenge.com/pc/hex/white.gif
# Username: butter; Password: fly
# Keyword:

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
        for i in range(10):
            hist = gif.histogram()  # 1 pixel in hist bin 8 (0-255)
            color = hist.index(1)
            print('Color bin: {}'.format(color))  # bin 8 out of 256
            data = list(gif.getdata())
            pixel_index = data.index(color)  # 20100
            indices.append(pixel_index)
            print('Pixel index: {}'.format(pixel_index))

            try:
                gif.seek(gif.tell() + 1)
                print('Frame: {}'.format(gif.tell() + 1))
            except EOFError:
                pass  # end of sequence

        print(indices)

        new = Image.new(gif.mode, gif.size)
        draw = ImageDraw.Draw(new)
        draw.line(first)
        draw.line(second)
        del draw

        new.save('./joystick_chall_22/final.jpg')

    return 0


if __name__ == '__main__':
    main()
