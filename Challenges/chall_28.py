#!/Applications/anaconda/envs/imgPIL/bin
# Python Challenge - 28
# http://www.pythonchallenge.com/pc/ring/bell.html
# http://www.pythonchallenge.com/pc/ring/green.html
# Username: repeat; Password: switch
# Keyword: guido

'''
Uses Anaconda environment with Pillow for image processing
    - Python 3.7, numpy, and Pillow (PIL)
    - Run `source activate imgPIL`, `python chall_28.py`
'''

from PIL import Image


def main():
    '''
    Hint: many pairs ring-ring, picture of waterfall
    RING-RING-RING say it out loud
    yes! green!
    '''
    with Image.open('./ring_chall_28/bell.png') as bell:
        w, h = bell.size  # (640, 480). Format: PNG; Mode: RGB
        # histo = bell.histogram()
        # print(histo[256:513])  # green pixels
        data = bell.getdata()
        green = [g for r, g, b in data]  # 307200 pixels

        # Get difference between green values next to each other
        tmp = [abs(green[i] - green[i + 1]) for i in range(0, len(green), 2)]
        # print(bytes(tmp).decode())
        # Remove the *'s (42)
        print(bytes(filter(lambda x: x != 42, tmp)).decode())

        # whodunnit().split()[0] ?

    return 0


if __name__ == '__main__':
    main()
