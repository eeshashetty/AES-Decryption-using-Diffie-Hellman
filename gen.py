from random import randint
P = 23 # prime
G = 9 # generator
    
# generating a public key
def gen_key(a):
    x = int(pow(G,a,P))
    return x

# generating a secret
def secret_key(x,a):
    k = int(pow(x,a,P))
    return k

import argparse

if __name__ == '__main__':
    a = 92
    b = 13
    # gets the generated key
    x = gen_key(a)
    y = gen_key(b)
    print('Public key of A: %d'%(y))
    print('Public key of B: %d'%(x))
    ka = secret_key(y,a)
    kb = secret_key(x,b)
    print('Secret key for the A is : %d'%(ka))
    print('Secret Key for the B is : %d'%(kb))