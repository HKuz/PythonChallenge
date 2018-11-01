#!/urs/local/bin/python3
# Python challenge - 20
# http://www.pythonchallenge.com/pc/hex/idiot2.html


import urllib.request


def main():
    '''
    Hint: go away! Picture is fence with sign 'Private property beyond
        this fence'
    But inspecting it carefully is allowed
    '''
    url = 'http://www.pythonchallenge.com/pc/hex/idiot2.html'
    username = 'butter'
    password = 'fly'

    with urllib.request.urlopen(
            url, data={'username': username, 'password': password}) as page:
        print(page.into())

    return 0

# Keyword:


if __name__ == '__main__':
    main()
