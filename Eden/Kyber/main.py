from random import randint

class Polynomial:
    def __init__(self, coefficients: list[int]):
        self.coefficients = coefficients
        self.order = len(self.coefficients) - 1

    def multiply(self, poly_2):
        product_polynomial = [0] * (self.order + poly_2.order + 1)
        order = len(product_polynomial) - 1

        for i in range(self.order + 1):
            for j in range(poly_2.order + 1):
                # print(product_polynomial, i, j)
                product_polynomial[i+j] += self.coefficients[i] * poly_2.coefficients[j]

        return Polynomial(product_polynomial)

    def add(self, poly_2):
        sum_polynomial = [0] * (max(self.order, poly_2.order) + 1)
        
        larger_polynomial = self.coefficients if self.order >= poly_2.order else poly_2.coefficients
        smaller_polynomial = self.coefficients if self.order < poly_2.order else poly_2.coefficients

        while len(smaller_polynomial) != len(larger_polynomial):
            smaller_polynomial.insert(0, 0)

        for i in range(len(larger_polynomial)):
            # print(i)
            # print(sum_polynomial)
            sum_polynomial[i] = larger_polynomial[i] + smaller_polynomial[i]
        
        return Polynomial(sum_polynomial)
    
    def subtract(self, poly_2):
        difference_polynomial = [0] * (max(self.order, poly_2.order) + 1)
        
        larger_polynomial = self.coefficients if self.order >= poly_2.order else poly_2.coefficients
        smaller_polynomial = self.coefficients if self.order < poly_2.order else poly_2.coefficients

        while len(smaller_polynomial) != len(larger_polynomial):
            smaller_polynomial.insert(0, 0)

        for i in range(len(larger_polynomial)):
            # print(i)
            # print(sum_polynomial)
            difference_polynomial_polynomial[i] = larger_polynomial[i] - smaller_polynomial[i]
        
        return Polynomial(difference_polynomial)

    
    def modular_reduce(self, modulus):
        for i in range(len(self.coefficients)):
            self.coefficients[i] %= modulus

    def upscale(self, n):
        for i in range(len(self.coefficients)):
            self.coefficients[i] *= n

    def __str__(self):
        return str(self.coefficients)


class Kyber:
    def __init__(self, max_degree, vector_size, mod_q, max_coefficient, max_error_coefficient):
        self.max_degree = max_degree
        self.vector_size = vector_size
        self.mod_q = mod_q
        self.max_coefficient = max_coefficient
        self.max_error_coefficient = max_error_coefficient
        # self.u_compression = u_compression
        # self.v_compression = v_compression

    def gen_keys(self): ## TODO: improve error distribution
        lattice = []

        for i in range(self.vector_size):
            row = []

            for j in range(self.vector_size):
                polynomial = []
                for k in range(self.max_degree):
                    polynomial.append(randint(0, self.max_coefficient))

                polynomial = Polynomial(polynomial)
                # print(polynomial)
                row.append(polynomial)

            lattice.append(row)

        # for i in lattice:
        #     for j in i:
        #         print(j)

        secret_key = []
        error_vector = []
        for i in range(self.vector_size):
            secret_key_polynomial_coefficients = []
            error_vector_polynomial_coefficients = []

            for j in range(self.max_degree):
                secret_key_polynomial_coefficients.append(randint(0, self.max_coefficient) % self.mod_q)
                error_vector_polynomial_coefficients.append(randint(0, self.max_error_coefficient) % self.mod_q)

            secret_key.append(Polynomial(secret_key_polynomial_coefficients))
            error_vector.append(Polynomial(error_vector_polynomial_coefficients))
        # print(secret_key[0])
        # print(error_vector[0])
        

        t = []

        for i in range(self.vector_size):
            polynomial = Polynomial([0])

            for j in range(self.vector_size): # matrix multiplication
                addition_polynomial = lattice[i][j].multiply(secret_key[j])
                polynomial = polynomial.add(addition_polynomial)

            polynomial = polynomial.add(error_vector[i])
            polynomial.modular_reduce(self.mod_q)
            print(polynomial)
            t.append(polynomial)

        public_key = (lattice, t)
        print(t)

        return public_key, secret_key

    def encrypt_message(self, message, public_key):
        #assume message = 1 int for now

        randomiser_vector, error_vector = [], []
        for _ in range(self.vector_size):
            polynomial_array_1, polynomial_array_2 = [], []

            for _ in range(self.max_degree):
                polynomial_array_1.append(randint(0, self.max_error_coefficient) % self.mod_q)
                polynomial_array_2.append(randint(0, self.max_error_coefficient) % self.mod_q)

            randomiser_vector.append(Polynomial(polynomial_array_1))
            error_vector.append(Polynomial(polynomial_array_2))

        error_polynomial = []
        for _ in range(self.max_degree):
            error_polynomial.append(randint(0, self.max_error_coefficient) % self.mod_q)
        error_polynomial = Polynomial(error_polynomial)

        message = Polynomial([int(c) for c in bin(message)[2:]])
        message.upscale(round(self.mod_q/2))
        message.modular_reduce(self.mod_q) # int to bin to list of 1s and 0s to that * round(q/2) reduced mod q

        # transposition matrix
        lattice = public_key[0]
        lattice_T = []
        for i in range(self.vector_size):
            row = []
            for j in range(self.vector_size):
                row.append(lattice[j][i])
            lattice_T.append(row)
            
        poly_vector_u = []
        for i in range(self.vector_size):
            polynomial = Polynomial([0])
            for j in range(self.vector_size):
                polynomial = polynomial.add(lattice_T[i][j].multiply(randomiser_vector[j]))
            polynomial = polynomial.add(error_vector[i])
            polynomial.modular_reduce(self.mod_q)
            poly_vector_u.append(polynomial)

        t = public_key[1]
        poly_v = Polynomial([0])
        # print(t)

        for i in range(self.vector_size):
            poly_v = poly_v.add(t[i].multiply(randomiser_vector[i]))
        poly_v = poly_v.add(error_polynomial).add(message)
        
        return (poly_vector_u, poly_v)

    # def decrypt_message(self, ciphertext, secret_key):
    #     poly_vector_u = ciphertext[0]
    #     sk_x_u = []
    #     for i in range()
        
        


if __name__ == "__main__":
    poly1 = Polynomial([2, 1, 2])
    poly2 = Polynomial([3, 0, 3, 7])
    print(poly1.add(poly2))
