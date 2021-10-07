from binascii import unhexlify

string = '73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d'
decoded = unhexlify(string)

def xor_single_byte(s1, key):
    output = b''
    for i in s1:
        output += bytes([i ^ key])
    try:
        return output.decode('utf-8')
    except:
        return "Exception occured"
results = {}
for i in range(1,256):
    results[i] = xor_single_byte(decoded, i)

for a,b in zip(results.values(),results.keys()):
    if "crypto" in a:
        print(a,"KEY:[{}]".format(b))