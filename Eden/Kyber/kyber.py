from polynomial import Polynomial
import numpy as np
import math
import random

class Kyber:

    def __init__(
            self,
            max_degree: int,
            order: int,
            mod_q: int,
            max_small_num: int
            ) -> None:

        self.max_degree = max_degree
        self.order = order

        self.mod_q = mod_q
        mod_f = [0] * (max_degree+1)
        mod_f[0] = 1
        mod_f[-1] = 1
        mod_f = Polynomial(mod_f)

        self.mod_func_poly = lambda poly: poly % mod_f % mod_q
        self.mod_func_mat = lambda row: self.mod_func_poly(row)

        self.max_small_num = max_small_num

    def gen_keys(self) -> tuple[
                            tuple[np.array(Polynomial),
                                  np.array(Polynomial)],
                        np.array(Polynomial)]:
        ''' Takes nothing as input, based on attributes as object
            Returns (public key, private key), where public key is a pair of 2 matrices of polynomials (A, t) and the private key is a single matrix of polynomials (s)
        '''
        s = []
        for i in range(self.order):
            poly = []
            for j in range(self.max_degree+1):
                poly.append(random.randint(0-self.max_small_num, self.max_small_num))
            s.append([Polynomial(poly)])

        A = []
        for i in range(self.order):
            row = []
            for j in range(self.order):
                poly = []
                for k in range(self.max_degree+1):
                    poly.append(random.randint(0, self.mod_q))
                row.append(Polynomial(poly))
            A.append(row)
        A = np.array(A)
    
        e = []
        for i in range(self.order):
            poly = []
            for j in range(self.max_degree+1):
                poly.append(random.randint(0-self.max_small_num, self.max_small_num))
            e.append([Polynomial(poly)])

        t = np.matmul(A, s) + e
        t = self.mod_func_mat(t)
        
        return ((A, t), s)
    
    def encrypt(
            self,
            plaintext: int,
            pub_key: tuple[np.array(Polynomial), np.array(Polynomial)]
            ) -> tuple[np.array(Polynomial), Polynomial]:
        # r = np.array([
        #         [Polynomial([-1, 1, 0, 0])],
        #         [Polynomial([1, 1, 0, -1])]
        #     ])
        r = []
        for i in range(self.order):
            poly = []
            for j in range(self.max_degree+1):
                poly.append(random.randint(0-self.max_small_num, self.max_small_num))
            r.append([Polynomial(poly)])
        # e1 = np.array([
        #         [Polynomial([1, 1, 0])],
        #         [Polynomial([1, 0, 0])]
        #     ])
        e1 = []
        for i in range(self.order):
            poly = []
            for j in range(self.max_degree+1):
                poly.append(random.randint(0-self.max_small_num, self.max_small_num))
            e1.append([Polynomial(poly)])
        # e2 = Polynomial([-1, -1, 0, 0])
        e2 = []
        for i in range(self.max_degree+1):
            e2.append(random.randint(0-self.max_small_num, self.max_small_num))
        e2 = Polynomial(e2)

        binary_msg = Polynomial(list(map(int, bin(plaintext)[2:])))
        upscaled_msg = binary_msg * normal_round(self.mod_q / 2)

        A = pub_key[0]
        t = pub_key[1]
        
        u = np.matmul(np.transpose(A), r) + e1
        u = self.mod_func_mat(u)

        v = np.matmul(np.transpose(t), r) + e2 + upscaled_msg
        v = self.mod_func_mat(v)[0][0]

        return (u, v)
    
    def decrypt(self, ciphertext: tuple[np.array(Polynomial), Polynomial], priv_key: np.array(Polynomial)) -> int:
        u = ciphertext[0]
        v = ciphertext[1]
        s = priv_key
        
        msg = self.mod_func_poly(v - np.matmul(np.transpose(s), u)[0][0])

        round_val = normal_round(self.mod_q/2)
        for i in range(len(msg.coefficients)):
            n = msg.coefficients[i]
            if abs(n - 0) < abs(n - round_val) or abs(n - self.mod_q) < abs(n - round_val):
                msg.coefficients[i] = 0
            else:
                msg.coefficients[i] = 1

        return int("".join([str(n) for n in msg.coefficients]), 2)

def normal_round(n: int) -> int:
    if n - math.floor(n) < 0.5:
        return math.floor(n)
    return math.ceil(n)

def poly_mat_str(mat: np.array(Polynomial)) -> str:
    out = ""
    for row in mat:
        for poly in row:
            out += str(poly) + ", "
        out += "\n"
    return out