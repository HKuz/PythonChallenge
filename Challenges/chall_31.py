#!/Applications/anaconda/envs/imgPIL/bin
# Python Challenge - 31
# http://www.pythonchallenge.com/pc/ring/grandpa.html
# http://www.pythonchallenge.com/pc/rock/grandpa.html
# Username: repeat; Password: switch
# Keyword: kohsamui, thailand; arecibo

'''
Uses Anaconda environment with Pillow for image processing
    - Python 3.7, numpy, and Pillow (PIL)
    - Run `source activate imgPIL`, `python chall_31.py`
'''

from PIL import Image


def main():
    '''
    Hint: where am I? Picture of rock near a beach
    short break, this ***REALLY*** has nothing to do with Python
    Login required: island: country -> search for Grandpa rock
    Next page:
    UFO's ?
    That was too easy. You are still on 31...
    Window element with iterations attribute of 128
    '''
    left = 0.34
    top = 0.57
    width = 0.036  # x-axis = reals
    height = 0.027  # y-axis = imaginaries
    max_iter = 128

    with Image.open('./mandelbrot_chall_31/mandelbrot_copy.gif') as mb:
        w, h = mb.size
        print('W: {}, H: {}'.format(w, h))
        r_step = width / w
        i_step = height / h
        new_data = []

        for y in range(h - 1, -1, -1):
            for x in range(w):
                c = complex(left + x * r_step, top + y * i_step)
                z = complex(0, 0)
                # f_c(z) = z^2 + c for f_c(0), f_c(f_c(0)), etc.
                for n_iter in range(max_iter):
                    z = z**2 + c
                    if abs(z) > 2:
                        break
                new_data.append(n_iter)

        new_mb = mb.copy()
        new_mb.putdata(new_data)
        new_mb.save('./mandelbrot_chall_31/new_mandelbrot.gif')

        # Find differences
        changes = [(a - b)for a, b in zip(mb.getdata(), new_mb.getdata())
                   if a != b]  # Length: 1679
        print(changes)
        factors = [n for n in range(2, int(len(changes) / 2) + 1) if
                   len(changes) % n == 0]  # [23, 73]

        # Create image from the differences
        new_new_mb = Image.new('1', tuple(factors))
        new_new_data = [1 if p >= 16 else 0 for p in changes]
        new_new_mb.putdata(new_new_data)
        new_new_mb.save('./mandelbrot_chall_31/message.gif')

    return 0


if __name__ == '__main__':
    main()
