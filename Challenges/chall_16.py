#!/Applications/anaconda/envs/pyEffy/bin
# Python challenge - 16
# www.pythonchallenge.com/pc/return/mozart.html

# Uses Anaconda environment with Pillow for image processing

from PIL import Image, ImageDraw

def main():
    '''
    Hint: let me get this straight
    Image has bars of 4 pink pixels with two white ones on ends
    '''
    photo_path = './mozart.gif'
    photo = Image.open(photo_path)
    width, height = photo.size # 640, 480
    # rgb(195, 195, 195)

    return 0

# Keyword: mozart


if __name__ == '__main__':
    main()
