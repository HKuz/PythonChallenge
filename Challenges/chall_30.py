#!/Applications/anaconda/envs/imgPIL/bin
# Python Challenge - 30
# http://www.pythonchallenge.com/pc/ring/yankeedoodle.html
# http://www.pythonchallenge.com/pc/ring/yankeedoodle.csv
# Username: repeat; Password: switch
# Keyword:

'''
Uses Anaconda environment with Pillow for image processing
    - Python 3.7, numpy, and Pillow (PIL)
    - Run `source activate imgPIL`, `python chall_30.py`
'''

from PIL import Image


def main():
    '''
    Hint: relax you are on 30; picture of beach scene
    The picture is only meant to help you relax
    while you look at the csv file
    '''
    with open('./relax_chall_30/yankeedoodle.csv') as csvfile:
        nums = [n.strip() for n in csvfile.read().split(',')]
        len_n = len(nums)  # 7367
        # float_nums = [float(s) for s in nums]
        # print('Max: {}, Min: {}'.format(max(float_nums), min(float_nums)))
        w, h = [n for n in range(2, int(len_n / 2) + 1) if
                len_n % n == 0]  # [53, 139]

        img = Image.new('P', (w, h))
        pixels = [int(float(n) * 256) for n in nums]
        img.putdata(pixels)
        img.save('./relax_chall_30/result.png')

    return 0


if __name__ == '__main__':
    main()
