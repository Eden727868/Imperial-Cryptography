import math
import random

def isPrime(n: int) -> bool:
    if n == 1:
        return False
    
    if n == 2:
        return True

    for i in range(2, math.floor(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True

def genPublicKey(phi_n: int) -> int:
    e = random.randint(3, phi_n - 1)

    while math.gcd(e, phi_n) != 1:
        e = random.randint(3, phi_n - 1)

    return e

def genPrivateKey(e: int, phi_n: int) -> int:
    for d in range(3, phi_n):
        if e * d % phi_n == 1:
            return d

max = 10000

primes = [n for n in range(1, max) if isPrime(n)]

p = primes[random.randint(0, len(primes)-1)]
print(p)

q = primes[random.randint(0, len(primes)-1)]
print(q)

phi_n = (p-1) * (q-1)
print(phi_n)

e = genPublicKey(phi_n)
print(e)

d = genPrivateKey(e, phi_n)
print(d)

