#!/usr/bin/python3

# ex
# USERNAME : aldeid
# PASSWORD : 6dephimh
# CORRECT , YOU WIN

name = input("Enter name:")
if len(name) > 2 and len(name) < 9: # name size 3 to 8
    dif = (len(name)//2)+1          # name/2 for shift, add 1 for decode (doing the reverse)
    back = ''.join( [ chr(ord(n)+dif) for n in name ] )
    pw = str(len(name)) + name[2] + back
    print("Pass: " + pw)
else:
    print("Invalid name")
