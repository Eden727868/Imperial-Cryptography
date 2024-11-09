from math import gcd
from random import randint, choice
from sys import argv
from utils import is_prime

def gen_publicKey(phi_n: int) -> int:
    e = randint(3, phi_n - 1)

    while gcd(e, phi_n) != 1:
        e = randint(3, phi_n - 1)

    return e

def gen_privateKey(e: int, phi_n: int) -> int:
    for d in range(3, phi_n):
        if e * d % phi_n == 1:
            return d

def cipher(plaintext: str, pub_key: int, n: int) -> str:
    encoded_message = [ord(char) for char in plaintext]
    encoded_message = [pow(num, pub_key, n) for num in encoded_message]
    ciphertext = " ".join([str(num) for num in encoded_message])

    return ciphertext

def decipher(ciphertext: str, priv_key: int, n: int) -> str:
    encoded_message = [pow(int(num), priv_key, n) for num in ciphertext.split()]
    plaintext = "".join([chr(num) for num in encoded_message])

    return plaintext

max = 1000
primes = [n for n in range(1, max) if is_prime(n)]


if __name__ == "__main__":
    p = choice(primes)
    print(p)

    q = choice(primes)
    print(q)
    
    n = p * q
    print(n)

    phi_n = (p-1) * (q-1)
    print(phi_n)

    e = gen_publicKey(phi_n)
    print(e)

    d = gen_privateKey(e, phi_n)
    print(d)

    text = input("Enter string:\n")

    ciphertext = cipher(text, e, n)
    print("Your encoded message is:\n" + ciphertext)

    deciphered_text = decipher(ciphertext, d, n)
    print("Your deciphered message is:\n" + deciphered_text)
