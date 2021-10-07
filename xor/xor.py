string = "label"

def XOR(a,b):
    return a^b

xored = ""
for i in string:
    xored += chr(XOR(ord(i),13))

print(xored)