#!/usr/local/bin/python3
# Python Challenge - 12
# http://www.pythonchallenge.com/pc/return/evil.html
# Username: huge; Password: file
# Keyword: disproportional


def main():
    '''
    Hint: Dealing evils.
    evil1.jpg -> evil2.jpg not .jpg - _.gfx -> evil3.jpg No more evils
    evil4.jpg -> can't be displayed because of errors (not a 404, though)
    Run: `curl -u huge:file http://www.pythonchallenge.com/pc/return/evil4.jpg`
        Returns: Bert is evil! Go back!
    evil2.gfx has 5 jpgs in it
    '''

    with open('./evils_chall_12/evil2.gfx', 'rb') as evil:
        evil = evil.read()

        for i in range(5):
            (open('./evils/evil_image' + str(i) + '.jpg', 'wb')
                .write(evil[i::5]))

    return 0


if __name__ == '__main__':
    main()
