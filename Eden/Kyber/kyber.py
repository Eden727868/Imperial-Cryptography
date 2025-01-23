from polynomial import Polynomial
import numpy as np
import math
import random

def gen_polynomial_modulus(max_degree: int) -> Polynomial:
    ''' Generates polynomial of the form x^max_degree + 1

        Used in Kyber cipher to restrict polynomials
        to a maximum degree of max_degree when performing
        binary operations on them
    '''
    poly = [0] * (max_degree)
    poly[0] = 1
    poly.append(1)
    return Polynomial(poly)

def normal_round(n: int) -> int:
    ''' Python rounds down some floats ending with 0.5
        This is used to round those upwards
    '''
    if n - math.floor(n) < 0.5:
        return math.floor(n)
    return math.ceil(n)

class Kyber:
    def __init__(
            self,
            max_degree:    int,
            order:         int,
            mod_q:         int,
            # max_small_num: int,
            eta_1:         int,
            eta_2:         int
            ) -> None:

        """ Takes 4 integers as parameters

            1st arg is the maximum polynomial degree
            2nd arg is the order of the matrices
            3rd arg is the prime modulus
            4th arg is the maximum small coefficient
        """ 

        self.max_degree = max_degree
        self.order = order

        self.mod_q = mod_q
        mod_f = gen_polynomial_modulus(max_degree)

        self.mod_fn_poly = lambda poly: poly % mod_f % mod_q
        self.mod_fn_matrix = lambda row: self.mod_fn_poly(row)

        # self.max_small_num = max_small_num
        self.eta_1 = eta_1
        self.eta_2 = eta_2
        self.rng = np.random.default_rng()

    def gen_keys(self) -> tuple[
                            tuple[np.array(Polynomial),
                                  np.array(Polynomial)],
                            np.array(Polynomial)
                            ]:
        ''' Takes nothing as input, keys generated are based on
            object attributes declared in initialisation

            Returns (public key, private key), where public key
            is a pair of 2 matrices of polynomials (A, t) and the
            private key is a single matrix of polynomials (s)
        '''
        s = []
        e = []
        for i in range(self.order):
            # s_poly = []
            # e_poly = []
            # s_poly = 
            # for j in range(self.max_degree+1):
            #     s_poly.append(random.randint(0-self.max_small_num, self.max_small_num))
            #     e_poly.append(random.randint(0-self.max_small_num, self.max_small_num))
            s_poly = self.rng.binomial(self.eta_1, 0.5, self.max_degree+1)
            e_poly = self.rng.binomial(self.eta_1, 0.5, self.max_degree+1)

            s.append([Polynomial(s_poly)])
            e.append([Polynomial(e_poly)])

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

        t = np.matmul(A, s) + e
        t = self.mod_fn_matrix(t)

        return ((A, t), s)

    def encrypt(
            self,
            plaintext: int,
            pub_key: tuple[np.array(Polynomial), np.array(Polynomial)]
            ) -> tuple[np.array(Polynomial), Polynomial]:

        ''' Takes plaintext (only as a single int) and public key (as a
            tuple of 2 matrices of polynomials) as input

            Returns a tuple with 1 matrix of polynomials and 1 single
            polynomial as the ciphertext
        '''
        r = []
        e1 = []
        for i in range(self.order):
            # r_poly = []
            # e_poly = []
            # for j in range(self.max_degree+1):
            #     r_poly.append(random.randint(0-self.max_small_num, self.max_small_num))
            #     e_poly.append(random.randint(0-self.max_small_num, self.max_small_num))
            r_poly = self.rng.binomial(self.eta_2, 0.5, self.max_degree+1)
            e_poly = self.rng.binomial(self.eta_2, 0.5, self.max_degree+1)
            r.append([Polynomial(r_poly)])
            e1.append([Polynomial(e_poly)])

        # e2 = []
        # for i in range(self.max_degree+1):
        #     e2.append(random.randint(0-self.max_small_num, self.max_small_num))
        e2 = Polynomial(self.rng.binomial(self.eta_2, 0.5, self.max_degree+1))

        binary_msg = Polynomial(list(map(int, bin(plaintext)[2:])))
        upscaled_msg = binary_msg * normal_round(self.mod_q / 2)

        A = pub_key[0]
        t = pub_key[1]

        u = np.matmul(np.transpose(A), r) + e1
        u = self.mod_fn_matrix(u)

        v = np.matmul(np.transpose(t), r) + e2 + upscaled_msg
        v = self.mod_fn_matrix(v)[0][0]

        return (u, v)

    def decrypt(
            self,
            ciphertext: tuple[np.array(Polynomial), Polynomial],
            priv_key: np.array(Polynomial)
            ) -> int:

        ''' Takes the ciphertext (a tuple of 1 matrix of polynomials and
            1 single polynomial) and a private key (1 matrix of polynomials)
            as input

            Returns an integer as the output
        '''
        u = ciphertext[0]
        v = ciphertext[1]
        s = priv_key

        msg = self.mod_fn_poly(v - np.matmul(np.transpose(s), u)[0][0])

        round_val = normal_round(self.mod_q/2)
        for i in range(len(msg.coefficients)):
            n = msg.coefficients[i]
            if abs(n - 0) < abs(n - round_val) or abs(n - self.mod_q) < abs(n - round_val):
                msg.coefficients[i] = 0
            else:
                msg.coefficients[i] = 1

        binary_string = "".join([str(n) for n in msg.coefficients])

        return int(binary_string, 2)
