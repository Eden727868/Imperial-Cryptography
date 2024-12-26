from polynomial import Polynomial
from kyber import Kyber
from random import randint
import numpy as np
from sys import argv

def poly_mat_str(mat: np.array(Polynomial)) -> str:
    out = ""
    for row in mat:
        for poly in row:
            out += str(poly) + ", "
        out += "\n"
    return out

def main() -> None:
    if len(argv) != 6:
        max_degree = int(input("Enter max polynomial degree (default 256): ").strip() or "256")
        order = int(input("Enter matrix order (default 4): ").strip() or "4")
        mod_q = int(input("Enter prime modulus (default 3329): ").strip() or "3329")
        max_sn = int(input("Enter max value for small coefficient (default 2): ").strip() or "2")

        msg = randint(0, 2**max_degree - 1)
        msg = int(input("Enter plaintext number (default random integer from 0 to 2^max degree -1): ").strip() or str(msg))
    else:
        max_degree = int(argv[1])
        order = int(argv[2])
        mod_q = int(argv[3])
        max_sn = int(argv[4])
        msg = int(argv[5])

    cipher = Kyber(max_degree, order, mod_q, max_sn)
    pub_key, priv_key = cipher.gen_keys()
    ciphertext = cipher.encrypt(msg, pub_key)
    plaintext = cipher.decrypt(ciphertext, priv_key)

    print("Public key:")
    print(poly_mat_str(pub_key[0]))
    print(poly_mat_str(pub_key[1]))
    print("Private key:")
    print(poly_mat_str(priv_key))
    print("Message: ", msg)
    print("Deciphered message:", plaintext)

if __name__ == "__main__":
    main()
