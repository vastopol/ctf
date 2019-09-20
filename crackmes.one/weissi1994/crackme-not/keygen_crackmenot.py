#!/usr/bin/python3

# password is first 8 char of name shift 5 to right

inp = input("Enter name:")
name = inp[:8]
passwd = ''.join([chr(ord(n)+5) for n in name])
print("Pass: " + passwd)

