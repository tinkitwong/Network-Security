import binascii
import struct

def KSA(key):
    keylength = len(key)
    S = list(range(256)) # type: range class
    # Add KSA implementation Here
    # reference code from KSA Section of https://en.wikipedia.org/wiki/RC4 
    j = 0
    for i in range(256):
        j = (j + S[i] + ord(key[i % keylength])) % 256
        S[i], S[j] = S[j], S[i]  # swap values of S[i] and S[j]
    return S

def PRGA(S):
    K = 0
    # Add PRGA implementation here
    # reference code from PRGA Section of https://en.wikipedia.org/wiki/RC4 
    i = 0
    j = 0
    while True:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i] # swap values of S[i] and S[j]
        K = S[(S[i] + S[j]) % 256]
        yield K

def RC4(key):
    S = KSA(key)
    return PRGA(S)

def convertKey(s):
    return [ord(c) for c in s]


if __name__ == '__main__':
    # RC4 algorithm please refer to http://en.wikipedia.org/wiki/RC4

    ## key = a list of integer, each integer 8 bits (0 ~ 255)
    ## ciphertext = a list of integer, each integer 8 bits (0 ~ 255)
    ## binascii.unhexlify() is a useful function to convert from Hex string to integer list

    key = "1A2B3C"
    ciphertext = '00112233'
    plaintext = "0F6D13BC"

    #key = convertKey(key)
    ## Use RC4 to generate keystream

    keystream = RC4(key)
    #print(type(next(keystream)))
    
    ## Cracking the ciphertext
    plaintext = ""
    for i in ciphertext:
        plaintext += ('{:02x}'.format(ord(i) ^ next(keystream)))
    print(plaintext)
    #     Several test cases: (to test RC4 implementation only)
    #     1. key = '1A2B3C', cipertext = '00112233' -> plaintext = '0F6D13BC'
    #     2. key = '000000', cipertext = '00112233' -> plaintext = 'DE09AB72'
    #     3. key = '012345', cipertext = '00112233' -> plaintext = '6F914F8F'
    
    
    
    ## Check ICV
