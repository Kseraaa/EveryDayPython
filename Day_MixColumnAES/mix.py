def mixColumns(a, b, c, d):
    printHex(gmul(a, 2) ^ gmul(b, 3) ^ gmul(c, 1) ^ gmul(d, 1))
    printHex(gmul(a, 1) ^ gmul(b, 2) ^ gmul(c, 3) ^ gmul(d, 1))
    printHex(gmul(a, 1) ^ gmul(b, 1) ^ gmul(c, 2) ^ gmul(d, 3))
    printHex(gmul(a, 3) ^ gmul(b, 1) ^ gmul(c, 1) ^ gmul(d, 2))
    print()

def gmul(a, b):
    if b == 1:
        return a
    tmp = (a << 1) & 0xff
    if b == 2:
        return tmp if a < 128 else tmp ^ 0x1b
    if b == 3:
        return gmul(a, 2) ^ a

def printHex(val):
    return print('{:02x}'.format(val), end=' ')

# test vectors from https://en.wikipedia.org/wiki/Rijndael_MixColumns#Test_vectors_for_MixColumn()
mixColumns(0x1A, 0x05, 0xB7, 0x7B) # 0x8e 0x4d 0xa1 0xbc
mixColumns(0xA3, 0xE1, 0xEA, 0x7C) # 0x9f 0xdc 0x58 0x9d
mixColumns(0x47, 0xB1, 0x37, 0xB5) # 0x01 0x01 0x01 0x01 
mixColumns(0xEC, 0x3A, 0x46, 0x22) # 0xc6 0xc6 0xc6 0xc6 


