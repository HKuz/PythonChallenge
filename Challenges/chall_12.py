#!/Applications/anaconda/envs/Python3/bin
# Python challenge - 12
# http://www.pythonchallenge.com/pc/return/evil.html


def main():
    '''
    Hint: Dealing evils.
    evil1.jpg -> evil2.jpg not .jpg - _.gfx -> evil3.jpg No more evils
    evil2.gfx has 5 jpgs in it
    '''

    with open('./evils/evil2.gfx', 'rb') as evil:
        evil = evil.read()

        for i in range(5):
            open('./evils/evil_image'+str(i)+'.jpg', 'wb').write(evil[i::5])

    return 0

# Keyword: disproportional


if __name__ == '__main__':
    main()
