from pwn import *
from pwnlib.util.fiddling import xor
from binascii import unhexlify
# KEY1 = a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313
# KEY2 ^ KEY1 = 37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e
# KEY2 ^ KEY3 = c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1
# FLAG ^ KEY1 ^ KEY3 ^ KEY2 = 04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf

def xor_2_strings(s1,s2):
    if len(s1)!= len(s2):
        return "Exception: the strings are not of equal length"
    else:
        return ''.join(format(int(a,base=16) ^ int(b,base=16) , 'x') for a,b in zip(s1,s2))


key1 = 'a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313'
key2 = xor_2_strings(key1, '37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e')
print("[-] KEY2: {}".format(key2))
key3 = xor_2_strings(key2, 'c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1')
print("[-] KEY3: {}".format(key3))
key4 = xor_2_strings(xor_2_strings(key1,key2),key3)
print("[-] KEY4: {}".format(key4))
flag =  xor_2_strings(key4, '04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf')
print("[*] FLAG: {}".format(unhexlify(flag)))



# flag = (key1 ^ key2 ^ key3)
# print(flag)