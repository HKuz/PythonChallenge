#!/Applications/anaconda/envs/imgPIL/bin
# Python Challenge - 7
# http://www.pythonchallenge.com/pc/def/hockey.html
# http://www.pythonchallenge.com/pc/def/oxygen.html
# Keyword: integrity

'''
Uses Anaconda environment with Pillow for image processing
    - Python 3.7, numpy, and Pillow (PIL)
    - Run `source activate imgPIL`, `python chall_07.py`
'''

import PIL
import PIL.Image


def main():
    '''
    Hint: photo with a stripe of grayscale boxes
    http://www.pythonchallenge.com/pc/def/oxygen.png
    '''
    photo = PIL.Image.open('./Resources/oxygen.png')
    pixel_access = photo.load()
    # print(photo.size) # (629, 95)
    width = photo.size[0]
    height = photo.size[1]

    # See how wide in pixels each gray box is - 1st is 5, rest 7
    # for i in range(50):
    #     print(pixel_access[i, height/2])

    # Create list comprehension of gray values
    first = [pixel_access[0, height / 2][0]]
    rest = [pixel_access[
        5 + 7 * i, height / 2][0] for i in range((width - 5) // 7)
    ]
    grays = first + rest
    message = ''.join([chr(item) for item in grays])
    print(message)

    # Get second message
    start_index = message.find('[')
    end_index = message.find(']')
    new_set = message[start_index + 1: end_index].split(',')
    final_message = ''.join([chr(int(item)) for item in new_set])
    print(final_message)

    return 0


if __name__ == '__main__':
    main()
