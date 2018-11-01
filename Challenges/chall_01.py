#!/usr/local/bin/python3
# Python challenge - 1
# http://www.pythonchallenge.com/pc/def/map.html


def main():
    '''
    Hint:
    K -> M
    O -> Q
    E -> G
    '''

    cipher_text = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

    plain_text = caesar_cipher(cipher_text, 2)
    print(plain_text)

    print(caesar_cipher('/map', 2))
    # change /map.html to /ocr.html


def caesar_cipher(cipher_text, n):
    '''
    Input: string of cipher_text, n is int for alphabet rotation
    Output: string of plain text, applying simple n rotation
    '''
    # Convert cipher_text to lowercase
    cipher_lower = cipher_text.lower()

    # Create cipher key dictionary
    codex = {}
    base = ord('a')

    for i in range(26):
        # Assumes a is 0, z is 25
        letter = chr(base + i)
        rotated_letter = chr(((i + n) % 26) + base)
        codex[letter] = rotated_letter

    # Build plain_text string using the codex mapping
    plain_text = ''

    for c in cipher_lower:
        plain_text += codex.get(c, c)

    return plain_text

# Keyword: ocr


if __name__ == '__main__':
    main()