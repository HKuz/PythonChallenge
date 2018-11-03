#!/usr/local/bin/python3
# Python Challenge - 13
# http://www.pythonchallenge.com/pc/return/disproportional.html
# http://www.pythonchallenge.com/pc/phonebook.php
# Username: huge; Password: file
# Keyword: italy

import xmlrpc.client


def main():
    '''
    Hint: phone that evil
    <area shape="circle" coords="326,177,45" href="../phonebook.php">
    '''
    xml_string = '<methodResponse><fault><value><struct><member><name>faultCode</name><value><int>105</int></value></member><member><name>faultString</name><value><string>XML error: Invalid document end at line 1, column 1</string></value></member></struct></value></fault></methodResponse>'
    server_url = 'http://www.pythonchallenge.com/pc/phonebook.php'

    with xmlrpc.client.ServerProxy(server_url) as server_proxy:
        print(server_proxy.system.listMethods())  # get a 'phone'
        print(server_proxy.system.methodHelp('phone'))
        print(server_proxy.system.methodSignature('phone'))
        try:
            print(server_proxy.phone('Bert'))  # 555-ITALY
        except Exception as e:
            print('Error', e)

    return 0


if __name__ == '__main__':
    main()
