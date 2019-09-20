#!/usr/bin/python3

# pass = name[0] + 2*name[1] + 2*name[2] + ... + 2*name[n]

name = input("Enter name:")
passwd = '0'
if name:
    nm = [ord(n)*2 for n in name[1:]]
    nmm = [ord(name[0])] + nm
    passwd = str(sum(nmm))
print("Pass: " + passwd)

