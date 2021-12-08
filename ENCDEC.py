import base64
from Crypto.Cipher import AES

BS = 16
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS).encode()
unpad = lambda s: s[:-ord(s[len(s)-1:])]
#GENERATE A (random hexadecimal number)
#temporaryKey = binascii.b2a_hex(os.urandom(16))

'''
Method:
 AES encryption
'''

def AESencrypt(key, message):
    cipher = AES.new(key, AES.MODE_ECB)
    raw = pad(message.encode())
    enc = cipher.encrypt(raw)
    return base64.b64encode(enc).decode('utf-8')

def AESdecrypt(key, enc):
    enc = base64.b64decode(enc)
    cipher = AES.new(key, AES.MODE_ECB)
    dec = cipher.decrypt(enc)
    return unpad(dec).decode('utf-8')

