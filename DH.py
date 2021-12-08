import ENCDEC
import os
import os.path
import hashlib
import argparse
global key
global prime_
from ENCDEC import AESencrypt, AESdecrypt

prime = 23
generator = 9
key_length = 600

def generate_secret(private_key, public_key):
    secret = pow(public_key, private_key, prime)
    try:
        secret_bytes = secret.to_bytes(secret.bit_length() // 8 + 1, byteorder="big")
    
    except AttributeError:
        secret_bytes = str(secret)
    
    #Generate hash key using SHA256
    key = hashlib.sha256()
    key.update(bytes(secret_bytes))
    secretKey = key.hexdigest()
    
    return secretKey

# Encrypt
def encrypt(filename,directory,public_key,private_key):
    key = generate_secret(int(private_key), int(public_key))
    key = key[0:32]
    file_obj = open(filename,"r")
    # Encode Message
    msg1 = AESencrypt(key, file_obj.read())
    outputFilename = os.path.join(directory,key[:16]+".txt")
    file_obj = open(outputFilename,'w')
    file_obj.write(msg1)
    return outputFilename, msg1

# Decrypt
def decrypt(filename,directory,public_key,private_key):
    # Generate Secret
    key = generate_secret(int(private_key), int(public_key))
    key = key[0:32]
    file_obj = open(filename,"r")
    msg = file_obj.read()
    # Decrypt Message
    text= AESdecrypt(key, msg)
    outputFilename = os.path.join(directory,"decrypted_file.txt")
    file_obj = open(outputFilename,"w")
    file_obj.write(text)
    return outputFilename, text

ap = argparse.ArgumentParser()
ap.add_argument("-f", "--file", required=True)
ap.add_argument("-o", "--output", required=True)
ap.add_argument("-m", "--mode", required=True)
args = vars(ap.parse_args())

if __name__ == "__main__":
    private_key = input("Enter Private Key: ")
    public_key = input("Enter Public Key: ")

    if(args["mode"] == "encrypt"):
        filename = args["file"]
        directory = args["output"]
        try:
            path, msg = encrypt(filename,directory,public_key,private_key)
            print("File Encrypted at "+path)
            print("Content: "+msg)
        except:
            print('\nERROR: Incorrect Public/Private Key')

    if(args["mode"] == "decrypt"):
        filename = args["file"]
        directory = args["output"]
        try:
            path,msg = decrypt(filename, directory, public_key, private_key)
            print("File Decrypted at "+path)
            print("\nMessage decrypted = "+msg)
        except:
            print('\nERROR: Incorrect Public/Private Key')  