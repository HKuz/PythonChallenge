#!/usr/local/bin/python3
# Python Challenge - 17
# http://www.pythonchallenge.com/pc/return/romance.html
# http://www.pythonchallenge.com/pc/return/cookies.html
# Username: huge; Password: file
# Keyword: balloons

import urllib.request
import urllib.parse
import http.cookiejar
import re
import bz2
import xmlrpc.client


def main():
    '''
    Hint: eat?
    Picture of chocolate chip cookies
    Embedded picture of saw thing from Nothings challenge (4)
    /cookies.html -> yummy! chocolate chips.
    Challenge 4:http://www.pythonchallenge.com/pc/def/linkedlist.html
        Inspect page -> Network -> Select page -> Cookies
    Cookies for page: you should have followed busynothing...
    '''
    base_url = ('http://www.pythonchallenge.com/pc/def/linkedlist'
                '.php?busynothing=')
    busynothing = '12345'
    # busynothing = '83051' # Cheat code
    pattern = re.compile(r'next busynothing is (\d+)')
    cookies = []
    cj = http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(
        urllib.request.HTTPCookieProcessor(cj)
    )

    while True:
        page = opener.open(base_url + busynothing)
        data = page.read().decode('utf-8')
        match = re.search(pattern, data)

        for c in cj:
            cookies.append(c.value)

        if match:
            busynothing = match.group(1)
        else:
            break

    raw_result = ''.join(cookies)
    '''
    raw_result = 'BZh91AY%26SY%94%3A%E2I%00%00%21%19%80P%81%11%00%AFg%9E%A0+%00
    hE%3DM%B5%23%D0%D4%D1%E2%8D%06%A9%FA%26S%D4%D3%21%A1%EAi7h%9B%9A%2B%BF%60%2
    2%C5WX%E1%ADL%80%E8V%3C%C6%A8%DBH%2632%18%A8x%01%08%21%8DS%0B%C8%AF%96KO%CA
    2%B0%F1%BD%1Du%A0%86%05%92s%B0%92%C4Bc%F1w%24S%85%09%09C%AE%24%90'
    '''

    result = urllib.parse.unquote_to_bytes(raw_result.replace('+', ' '))
    # result = urllib.parse.unquote_plus(raw_result, 'latin1').encode('latin1')
    decoded_result = bz2.decompress(result)
    print(decoded_result.decode('ascii'))
    '''
    is it the 26th already? call his father and inform him that
    "the flowers are on their way". he'll understand.
    '''

    server_url = 'http://www.pythonchallenge.com/pc/phonebook.php'

    with xmlrpc.client.ServerProxy(server_url) as server_proxy:
        try:
            print(server_proxy.phone('Leopold'))  # 555-VIOLIN
        except Exception as e:
            print('Error', e)

    # got to /violin.html: no! i mean yes! but ../stuff/violin.php.
    violin_url = 'http://www.pythonchallenge.com/pc/stuff/violin.php'
    message = 'the flowers are on their way'
    quoted = urllib.parse.quote_plus(message)
    request = urllib.request.Request(
        violin_url, headers={"Cookie": "info=" + quoted}
    )
    response = urllib.request.urlopen(request).read().decode()
    print(response)

    return 0


if __name__ == '__main__':
    main()
