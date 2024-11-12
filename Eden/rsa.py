from math import gcd
from random import randint, choice
from sys import argv
from utils import is_prime

def gen_rsa_public_key(phi_n: int) -> int:
    ''' Takes integer phi of n as input and returns integer public key as output
        Phi of n is the Euler Totient Function of n, returns the number of numbers less than and coprime with n
        If n is the product of 2 primes p and q, phi of n = (p-1) * (q-1)
        The public key is a random number between 3 and phi of n that is coprime with phi of n
    '''
    e = randint(3, phi_n - 1)

    while gcd(e, phi_n) != 1:
        e = randint(3, phi_n - 1)

    return e

def gen_rsa_private_key(e: int, phi_n: int) -> int:
    ''' Takes integers public key and phi of n as input and returns integer private key
        Phi of n is the Euler Totient Function of n, returns the number of numbers less than and coprime with n
        If n is the product of 2 primes p and q, phi of n is given by (p-1) * (q-1)
        The private key is the modular inverse of the public key mod phi of n
    '''
    for d in range(3, phi_n):
        if e * d % phi_n == 1:
            return d

def rsa_cipher(plaintext: str, pub_key: int, n: int) -> str:
    ''' Takes string plaintext, integer public key and integer n as input and returns string ciphertext as output
        ciphertext = plaintext ^ public key mod n
    '''
    encoded_message = [ord(char) for char in plaintext]
    encoded_message = [pow(num, pub_key, n) for num in encoded_message]
    ciphertext = " ".join([str(num) for num in encoded_message])

    return ciphertext

def rsa_decipher(ciphertext: str, priv_key: int, n: int) -> str:
    ''' Takes string ciphertext, integer private key and integer n as input and returns string plaintext as output
        plaintext = ciphertext ^ private key mod n 
    '''
    encoded_message = [pow(int(num), priv_key, n) for num in ciphertext.split()]
    plaintext = "".join([chr(num) for num in encoded_message])

    return plaintext

def rsa_sign(message: str, priv_key: int, n: int) -> str:
    ''' Takes string message, integer private key and integer n as input and returns string signed message as output
        signed message = message ^ private key mod n
        same algorithm as cipher() except takes private key as input instead of public key
    '''
    encoded_message = [pow(int(num), priv_key, n) for num in ciphertext.split()]
    encoded_message = [ord(char) for char in message]
    encoded_message = [pow(num, priv_key, n) for num in encoded_message]
    signed_message = " ".join([str(num) for num in encoded_message])

    return signed_message

def verify_rsa_signature(message: str, pub_key: int, n: int) -> str: # same algorithm as decipher except takes public key as input instead of public key
    ''' Takes string signed message, integer public key and integer n as input and returns string message as output
        message = signed message ^ public key mod n
        same algorithm as decipher() except takes public key as input instead of private key
    '''
    encoded_message = [pow(int(num), pub_key, n) for num in message.split()]
    unsigned_message = "".join([chr(num) for num in encoded_message])

    return unsigned_message

if __name__ == "__main__":
    if len(argv) != 2 or argv[1] not in ["0", "1", "2", "3", "4", "5"]:
        print("Execute program with a command-line argument")
        print("\t[0] to generate private and public keys")
        print("\t[1] to encode a message using a public key")
        print("\t[2] to decode a message using a private key")
        print("\t[3] to sign a message")
        print("\t[4] to verify a signature")
        quit()
    
    elif argv[1] == "0":
        max = int(input("Enter max prime value: "))
        primes = [n for n in range(1, max) if is_prime(n)]

        p = choice(primes)
        q = choice(primes)
        print(f"Primes: {p} and {q}")
        
        n = p * q
        print(f"N: {n}")

        phi_n = (p-1) * (q-1)

        e = gen_rsa_public_key(phi_n)
        print(f"Public key: {e}")

        d = gen_rsa_private_key(e, phi_n)
        print(f"Private key: {d}")

    elif argv[1] == "1":
        plaintext = input("Enter plaintext:\n")
        public_key = int(input("Enter public key: "))
        n = int(input("Enter N: "))

        ciphertext = rsa_cipher(plaintext, public_key, n)
        print(f"Your encoded message is:\n{ciphertext}")

    elif argv[1] == "2":
        ciphertext = input("Enter ciphertext:\n")
        private_key = int(input("Enter private key: "))
        n = int(input("Enter N: "))

        plaintext = rsa_decipher(ciphertext, private_key, n)
        print(f"Your plaintext message is:\n{plaintext}")

    elif argv[1] == "3":
        message = input("Enter message to be signed:\n")
        private_key = int(input("Enter private key: "))
        n = int(input("Enter N: "))

        signed_message = rsa_sign(message, private_key, n)
        print(f"Your signed message is:\n{signed_message}")

    elif argv[1] == "4":
        message = input("Enter signed message to verify:\n")
        private_key = int(input("Enter public key: "))
        n = int(input("Enter N: "))

        unsigned_message = verify_rsa_signature(message, public_key, n)
        print(f"Your unsigned message is:\n{unsigned_message}")
