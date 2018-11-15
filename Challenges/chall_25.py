#!/usr/local/bin/python3
# Python Challenge - 25
# http://www.pythonchallenge.com/pc/hex/lake.html
# Username: butter; Password: fly
# Keyword:

import os
import wave
import matplotlib.pyplot as plt
import numpy as np


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

    source_dir = './waves_chall_25/'
    wave_files = ['lake{}.wav'.format(i) for i in range(1, 26)]
    return 0


if __name__ == '__main__':
    main()
