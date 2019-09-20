#!/usr/bin/python3

# password can be any string of format where '@' is 5th char
# str = XXXX@XXXXX

inp = input("Enter pass:")

if len(inp) == 10 and inp[4] == '@':
    print("Valid pass")
else:
    print("Invalid pass")

