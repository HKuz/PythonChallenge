#!/Applications/anaconda/envs/imgPIL/bin
# Python Challenge - 25
# http://www.pythonchallenge.com/pc/hex/lake.html
# Username: butter; Password: fly
# Keyword: decent

'''
Uses Anaconda environment with Pillow for image processing
    - Python 3.7, numpy, and Pillow (PIL)
    - Run `source activate imgPIL`, `python chall_25.py`
'''

import wave
from PIL import Image


def main():
    '''
    Hint: imagine how they sound; picture of lake with puzzle pieces overlaid
    can you see the waves; name of image is lake1.jpg
    Download wave files 1-25: http://www.pythonchallenge.com/pc/hex/lake[N].wav
    Bash command (-o option writes to file vs. stdout, #1 refers to seq val
        to name the file, -U is proxy-user login info):

        curl -U butter:fly -o "./waves_chall_25/lake#1.wav"
        "http://www.pythonchallenge.com/pc/hex/lake[1-25].wav"
    '''

    waves = ['./waves_chall_25/lake{}.wav'.format(i) for i in range(1, 26)]
    w = 60  # Challenge image is 640x480, these values by trial and error
    h = 60

    # Look at wave file properties - all files are same
    '''
    with wave.open(wave_files[0], 'rb') as tmp:
        print('Frames: {}'.format(tmp.getnframes()))  # 10800
        print('Channels: {}'.format(tmp.getnchannels()))  # 1
        print('Samp width: {}'.format(tmp.getsampwidth()))  # 1
        print('Frame rate: {}'.format(tmp.getframerate()))  # 9600
        bytes_datum = tmp.readframes(tmp.getnframes())
        tmpimg = Image.frombytes('RGB', (w, h), bytes_datum)
        tmpimg.save('./waves_chall_25/test.jpg')
    '''

    # Convert each wave file to an image and combine into one
    img = Image.new('RGB', (w * 5, h * 5), color=(255, 255, 255))

    for i, filename in enumerate(waves):
        with wave.open(filename, 'rb') as wavfile:
            bytes_data = wavfile.readframes(wavfile.getnframes())
            wave_img = Image.frombytes('RGB', (w, h), bytes_data)
            img.paste(wave_img, ((i % 5) * w, (i // 5) * h))

    img.save('./waves_chall_25/final.jpg')

    return 0


if __name__ == '__main__':
    main()
