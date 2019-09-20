#!/usr/bin/python3

# ord(c) for c in pass must be 1000 including the newline
# input strips newline so add 0xa == 10 to x

inp = input("Enter pass:")
msg = "Invalid pass"
tot = sum([ord(c) for c in inp]) + 10
if len(inp) < 11 and tot == 1000:
    msg = "Valid pass"
print(tot,msg)

