from polynomial import Polynomial
from kyber import Kyber
import numpy as np

def poly_mat_str(mat: np.array(Polynomial)) -> str:
    out = ""
    for row in mat:
        for poly in row:
            out += str(poly) + ", "
        out += "\n"
    return out

def main() -> None:
    max_degree = int(input("Enter max polynomial degree (default 256): ").strip() or "256")
    order = int(input("Enter matrix order (default 4): ").strip() or "4")
    mod_q = int(input("Enter prime modulus (default 3329): ").strip() or "3329")
    max_sn = int(input("Enter max value for small coefficient (default 2): ").strip() or "2")

    msg = int(input("Enter plaintext number (default 12): ").strip() or "12")

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
