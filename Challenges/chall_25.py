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
    '''

    source_dir = './waves_chall_25/'

    plt.figure(figsize=(20, 20))
    plot_index = 1
    for filename in os.listdir(source_dir):
        if filename == ".DS_Store":
            continue

        with wave.open(source_dir + filename, "rb") as spf:
            # Extract Raw Audio from File
            signal = spf.readframes(-1)
            signal = np.fromstring(signal, "Int16")

            # Split the data into channels [COMMENTED OUT]
            # channels = [[] for channel in range(spf.getnchannels())]
            # for index, datum in enumerate(signal):
            #     channels[index % len(channels)].append(datum)

            # Get time from indices
            fs = spf.getframerate()  # sampling frequency
            time = np.linspace(0, len(signal) / fs, num=len(signal))
            # Channel time calculation
            # time = np.linspace(0, len(signal) / len(channels) / fs,
            #                    num=len(signal) / len(channels))

        plt.subplot(5, 5, plot_index)
        plt.tight_layout()
        plt.title("Signal: {}".format(filename[:-4]))
        plt.axis(ymin=-9000, ymax=9000)
        plt.plot(time, signal)
        # for channel in channels:
        #     plt.plot(time, channel)
        plot_index += 1

    plt.savefig("SignalWavePlots.pdf")
    plt.show()
    plt.clf()

    return 0


if __name__ == '__main__':
    main()
