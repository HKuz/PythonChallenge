#!/urs/local/bin/python3
# Python challenge - 19
# http://www.pythonchallenge.com/pc/hex/bin.html

import base64
import wave
import audioop


def main():
    '''
    Hint: please! Photo is a map of India

    <!--
    From: leopold.moz@pythonchallenge.com
    Subject: what do you mean by "open the attachment?"
    Mime-version: 1.0
    Content-type: Multipart/mixed; boundary="===============1295515792=="

    It is so much easier for you, youngsters.
    Maybe my computer is out of order.
    I have a real work to do and I must know what's inside!

    --===============1295515792==
    Content-type: audio/x-wav; name="indian.wav"
    Content-transfer-encoding: base64

    <moved to indian.wav>

    --===============1295515792==--

    -->

    sorry.html (www.pythonchallenge.com/pc/hex/.html) ->
        -"what are you apologizing for?"
    '''
    # Decode base64 encoding, write to a wav file?
    with open('./indian.txt', 'r') as rawtext:
        data = rawtext.read()
        decoded_bytes = base64.b64decode(data)
        temp = open('./temp.wav', 'wb')
        temp.write(decoded_bytes)
        temp.close()

    temp_wav = wave.open('./temp.wav', 'rb')
    indian = wave.open('./indian.wav', 'wb')
    bigindian = wave.open('./bigindian.wav', 'wb')

    nchannels, sampwidth, framerate, nframes, comptype, compname = \
        temp_wav.getparams()
    print('Number audio channels (1 mono, 2 stereo): {}\nSample width in bits: {}\nSample freq (frame rate): {}\nNumber audio frames: {}\nCompression type (NONE is only supported type): {}\nHuman-readable compression type: {}'.format(nchannels, sampwidth, framerate, nframes, comptype, compname))

    frames = temp_wav.readframes(nframes)
    frames_swap = audioop.byteswap(frames, sampwidth)

    indian.setparams(
        (nchannels, sampwidth, framerate, nframes, comptype, compname))
    bigindian.setparams(
        (nchannels, sampwidth, framerate, nframes, comptype, compname))

    indian.writeframes(frames)  # little endian -> 'sorry'
    bigindian.writeframes(frames_swap)
    # big endian -> 'you are an idiot, ah ah ah ah ah ah ah'

    temp_wav.close()
    indian.close()
    bigindian.close()

    return 0

# Keyword: sorry, idiot


if __name__ == '__main__':
    main()
