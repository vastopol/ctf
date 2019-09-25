#!/usr/bin/python

import hashlib
import sys

TIME = 1
output = ""
email = "jkr@writeup.htb"
salt = '5a599ef579066807'
password = "62def4866937f08cc13bab43bb14e6f7"
wordlist = sys.argv[1]

def crack_password():
    global password
    global output
    global wordlist
    global salt
    dict = open(wordlist)
    for line in dict.readlines():
        line = line.replace("\n", "")
        if hashlib.md5(str(salt) + line).hexdigest() == password:
            print password, ":", hashlib.md5(str(salt) + line).hexdigest()
            print "Hash:", hashlib.md5(str(salt) + line).hexdigest()
            output += "\n[+] Password cracked: " + line
            print "Output:", output
            break
    dict.close()

crack_password();
