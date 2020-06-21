#!/usr/bin/python3

import base64
import hashlib
import os
import sys

i = 0
target = sys.argv[1]

while True:
    m = hashlib.md5()
    m.update(str(i).encode())
    h = m.hexdigest()
    if h[:6] == target:
        print(i)
        exit(0)
    i += 1
