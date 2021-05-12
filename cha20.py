from Crypto.Cipher import ChaCha20
from Crypto.Random import get_random_bytes
import base64
import random
import sys
import codecs
import json

def encrypt(text,key):
    key = key.encode('utf-8')
    cipher = ChaCha20.new(key=key)
    ciphertext = cipher.encrypt(text)
    nonce = base64.b64encode(cipher.nonce.hex().encode('utf-8'))
    cshell = base64.b64encode(ciphertext.hex().encode('utf-8'))
    return [str(nonce,'utf-8'),str(cshell,'utf-8'),ciphertext,cipher.nonce]
    #return ciphertext

def getkey():
    randstr = random.sample('qazwsxedcrfvtgbyhnujmikolpQAZWSXEDCRFVTGBYHNUJMIKOLP1234567890',32)
    key = (''.join(randstr))
    return key
shellcode = b''#shellcode
deshellcode = codecs.escape_decode(shellcode)[0]
hexshellcode = deshellcode.hex()
enshellcode = base64.b64encode(hexshellcode.encode('utf-8'))
key = getkey()
cshell = encrypt(enshellcode,key)
jsonpost = json.dumps({'key':key,'nonce':cshell[0],'ciphertext':cshell[1]})
print(jsonpost)
