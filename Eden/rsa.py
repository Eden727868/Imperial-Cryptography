import math
import random
from utils import is_prime

def gen_publicKey(phi_n: int) -> int:
    e = random.randint(3, phi_n - 1)

    while math.gcd(e, phi_n) != 1:
        e = random.randint(3, phi_n - 1)

    return e

def gen_privateKey(e: int, phi_n: int) -> int:
    for d in range(3, phi_n):
        if e * d % phi_n == 1:
            return d

max = 10000

primes = [n for n in range(1, max) if is_prime(n)]

p = primes[random.randint(0, len(primes)-1)]
print(p)

q = primes[random.randint(0, len(primes)-1)]
print(q)

phi_n = (p-1) * (q-1)
print(phi_n)

e = gen_publicKey(phi_n)
print(e)

d = gen_privateKey(e, phi_n)
print(d)

