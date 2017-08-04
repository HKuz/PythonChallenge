#!/urs/local/bin/python3
# Python challenge - 6
# http://www.pythonchallenge.com/pc/def/channel.html
# http://www.pythonchallenge.com/pc/def/channel.zip

import re
import zipfile


def main():
    '''
    Hint: zip, now there are pairs

    In the readme.txt:
    welcome to my zipped list.

    hint1: start from 90052
    hint2: answer is inside the zip

    Last nothing = 46145
    Collect the comments
    '''
    nothing = '90052'
    file_ext = '.txt'
    file_pattern = re.compile(r'Next nothing is (\d+)')
    zf = zipfile.ZipFile('channel.zip')
    comments = []

    while True:
        filename = nothing + file_ext
        data = zf.read(filename).decode('utf-8')
        match = re.search(file_pattern, data)
        if match:
            nothing = match.group(1)
            comments.append(zf.getinfo(filename).comment.decode('utf-8'))
        else:
            break

    # print('Last nothing is: {}'.format(nothing))
    print(''.join(comments))

    return 0

# Keyword: hockey


if __name__ == '__main__':
    main()
