#!/usr/local/bin/python3
# Python Challenge - 29
# http://www.pythonchallenge.com/pc/ring/guido.html
# Username: repeat; Password: switch
# Keyword:

import base64
import urllib.request


def main():
    '''
    Hint: silence!
    whoisit.jpg
    '''
    url = 'http://www.pythonchallenge.com/pc/ring/guido.html'
    # auth = 'Basic cmVwZWF0OnN3aXRjaA=='
    auth = base64.b64encode(b'repeat:switch').decode()
    headers = {'Authorization': 'Basic {}'.format(auth)}

    request = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(request)
    source = response.read().decode()
    index = source.find('</html>') + len('</html>\n')
    silence = source[index:]
    print(silence)

    return 0


if __name__ == '__main__':
    main()
