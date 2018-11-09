#!/usr/local/bin/python3
# Python Challenge - 20
# http://www.pythonchallenge.com/pc/hex/idiot2.html
# Username: butter; Password: fly
# Keyword:

import urllib.request
import base64
import urllib.parse


def main():
    '''
    Hint: go away! Picture is fence with sign 'Private property beyond
        this fence'
    But inspecting it carefully is allowed
    '''
    # url = 'http://www.pythonchallenge.com/pc/hex/idiot2.html'
    url = 'http://www.pythonchallenge.com/pc/hex/unreal.jpg'
    # Looking at headers on page, see Authorization: Basic YnV0dGVyOmZseQ==
    # Use b64 encoding to get value, decode() to change from byte to str
    auth = base64.b64encode(b'butter:fly').decode()
    # content_type = ('Mozilla/5.0 (Macintosh; Intel Mac OS X x.y; rv:42.0)'
    #                 'Gecko/20100101 Firefox/62.0')

    headers = {
        # 'User-Agent': content_type,
        'Authorization': 'Basic {}'.format(auth)
    }

    request = urllib.request.Request(url, headers=headers)
    # print(request.headers)
    response = urllib.request.urlopen(request)
    print(response.headers)  # Content-Range: bytes 0-30202/2123456789
    request.add_header()

    return 0


if __name__ == '__main__':
    main()


# headers={'username': username, 'password': password}
