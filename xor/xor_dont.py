from binascii import *
from pwn import *

msg = '0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104'
decoded = unhexlify(msg)

def xor(msg, key):
    o = ''
    for i in range(len(msg)):
        o += chr((msg[i]) ^ ord(key[i % len(key)]))
    return o
  
# Phase 1 - Find part of key
part_of_msg = 'crypto{'

for i in range(len(decoded)):
    candidate = xor(decoded[i:i+len(part_of_msg)], part_of_msg)
    if candidate.isalnum():
        print(candidate)
flag = xor(decoded,'myXORkey')
print(flag)

#alternative solution
# from pwn import *
# text = bytes.fromhex('0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104')

# key = xor(text, 'crypto')
# print(key)