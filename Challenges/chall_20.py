#!/usr/local/bin/python3
# Python Challenge - 20
# http://www.pythonchallenge.com/pc/hex/idiot2.html
# Username: butter; Password: fly
# Keyword: invader, redavni

import base64
import urllib.request
import re


def main():
    '''
    Hint: go away! Picture is fence with sign 'Private property beyond
        this fence'
    But inspecting it carefully is allowed
    '''
    url = 'http://www.pythonchallenge.com/pc/hex/unreal.jpg'
    # Looking at headers on page, see Authorization: Basic YnV0dGVyOmZseQ==
    # Use b64 encoding to get value, decode() to change from byte to str
    auth = base64.b64encode(b'butter:fly').decode()
    headers = {'Authorization': 'Basic {}'.format(auth)}

    request = urllib.request.Request(url, headers=headers)
    # print(request.headers)
    response = urllib.request.urlopen(request)
    # print(response.getcode())  # 200, type -> int
    # print(response.headers)
    '''
    HEADER:
    Content-Type: image/jpeg
    Content-Range: bytes 0-30202/2123456789
    Connection: close
    Transfer-Encoding: chunked
    Date: Fri, 09 Nov 2018 16:44:12 GMT
    Server: lighttpd/1.4.35
    '''

    messages, content_ranges = [], []
    regex = re.compile(r'bytes\s?(\d+-(\d+))/(\d+)')

    while True:
        try:
            match = regex.search(response.headers['Content-Range'])
            endbytes, total_size = match.group(2), match.group(3)
            content_ranges.append(match.group(1))
            request.headers['Range'] = 'bytes={}-'.format(int(endbytes) + 1)
            response = urllib.request.urlopen(request)
            message = response.read().decode()
            messages.append(message)
            # print(message, end='')
        except urllib.error.HTTPError:
            # Break for HTTP Error 416: Requested Range Not Satisfiable
            break

    '''
    Why don't you respect my privacy?
    we can go on in this way for really long time.
    stop this!
    invader! invader!
    ok, invader. you are inside now.
    '''

    # Try to request bytes after size
    request.headers['Range'] = 'bytes={}-'.format(int(total_size) + 1)
    response = urllib.request.urlopen(request)
    match = regex.search(response.headers['Content-Range'])
    content_ranges.append(match.group(1))
    message = response.read().decode()
    # the password is your new nickname in reverse: redavni
    messages.append(message[::-1])

    # print(''.join(messages))
    # print('Content Ranges:')
    # print('\n'.join(content_ranges))

    '''
    HEADER:
    Content-Type: application/octet-stream
    Content-Transfer-Encoding: binary
    Content-Range: bytes 2123456744-2123456788/2123456789
    Connection: close
    Transfer-Encoding: chunked
    Date: Fri, 09 Nov 2018 18:26:03 GMT
    Server: lighttpd/1.4.35

    All Content Ranges:
    0-30202
    30203-30236
    30237-30283
    30284-30294
    30295-30312
    30313-30346
    2123456744-2123456788
    '''

    # Search the bytes in reverse
    range_val = int(content_ranges[-1].split('-')[0])  # 2123456744
    request.headers['Range'] = 'bytes={}-'.format(int(range_val) - 1)
    response = urllib.request.urlopen(request)
    match = regex.search(response.headers['Content-Range'])
    content_ranges.append(match.group(1))
    message = response.read().decode()
    messages.append(message)
    # and it is hiding at 1152983631

    # Get what's hiding
    request.headers['Range'] = 'bytes=1152983631-'
    response = urllib.request.urlopen(request)
    match = regex.search(response.headers['Content-Range'])
    content_ranges.append(match.group(1))
    with open('./invader_chall_20/message.zip', 'wb') as file:
        file.write(response.read())

    '''
    Yes! This is really level 21 in here.
    And yes, After you solve it, you'll be in level 22!

    Now for the level:

    * We used to play this game when we were kids
    * When I had no idea what to do, I looked backwards.
    '''

    return 0


if __name__ == '__main__':
    main()


# headers={'username': username, 'password': password}
