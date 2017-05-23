#!/Applications/anaconda/envs/Python3/bin
# Python challenge - 2
# http://www.pythonchallenge.com/pc/def/ocr.html

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
letters = []

with open('garbage.txt', 'r') as garbage:
    for line in garbage.readlines():
        for c in line:
            if c in alphabet:
                letters.append(c)

print(''.join(letters))

# Keyword: equality
