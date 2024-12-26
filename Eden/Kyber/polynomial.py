from itertools import zip_longest

class Polynomial:

    def __init__(self, coefficients: list[int]) -> None:
        ''' Coefficients are of descending order of degree (x^3, x, x^2, ...)
        '''
        self.coefficients = coefficients

    def get_degree(self) -> int:
        return len(self.coefficients)-1

    def clean(self) -> None:
        try:
            while self.coefficients[0] == 0:
                del self.coefficients[0]
        except:
            self.coefficients = []

    def __add__(self, other) -> 'Polynomial':
        coefficients = [x+y for x,y in zip_longest(reversed(self.coefficients), reversed(other.coefficients), fillvalue=0)][::-1]
        output = Polynomial(coefficients)
        output.clean()
        return output

    def __sub__(self, other) -> 'Polynomial':
        coefficients = [x-y for x,y in zip_longest(reversed(self.coefficients), reversed(other.coefficients), fillvalue=0)][::-1]
        output = Polynomial(coefficients)
        output.clean()
        return output

    def __mul__(self, other) -> 'Polynomial':
        if type(other) == Polynomial:
            degree = self.get_degree() + other.get_degree()
            coefficients = [0 for _ in range(degree+1)]

            for i in range(len(self.coefficients)):
                for j in range(len(other.coefficients)):
                    product = self.coefficients[i] * other.coefficients[j]
                    current_degree = degree - i - j
                    coefficients[current_degree] += product

            coefficients = coefficients[::-1]
            
            output = Polynomial(coefficients)
            output.clean()
            return output
        elif type(other) == int:
            coefficients = [n * other for n in self.coefficients]
            return Polynomial(coefficients)

    def __floordiv__(self, other: int) -> 'Polynomial':
        coefficients = [n // other for n in self.coefficients]
        return Polynomial(coefficients)

    def __mod__(self, other) -> 'Polynomial':
        if type(other) == int:
            coefficients = [n % other for n in self.coefficients]
            return Polynomial(coefficients)

        elif type(other) == Polynomial:
            target_degree = other.get_degree()
            output = Polynomial(self.coefficients)
            
            while output.get_degree() >= target_degree:
                subtraction_coefficients = [output.coefficients[0]]
                for i in range(1, output.get_degree() - target_degree + 1):
                    subtraction_coefficients.append(0)

                subtraction_polynomial = Polynomial(subtraction_coefficients)
                subtraction_polynomial *= other
                
                output -= subtraction_polynomial
            
            return output

    def __str__(self) -> str:
        out = ""

        for i in range(self.get_degree()):
            current_power = self.get_degree() - i
            out += str(self.coefficients[i]) + "x^" + str(current_power) + " + "
        out += str(self.coefficients[-1])

        return out


def main() -> None:
    p = Polynomial([1, 2, 3])
    q = Polynomial([4, 5, 6])
    r = Polynomial([7, 8])
    s = Polynomial([9, 10, 11, 12])

    # print("P:", p)
    # print("Q:", q)
    # print("P+Q:", p+q)
    # print("R:", r)
    # print("P+R:", p+r)
    # print("S:", s)
    # print("P+S:", p+s)
    # # Success

    # print("P:", p)
    # print("Q:", q)
    # print("R:", r)
    # print("S:", s)
    # print("P*Q:", p*q)
    # print("P*R:", p*r)
    # print("P*S:", p*s)
    # # Success

    # t = Polynomial([1, 0, 1])
    # print("P:", p)
    # print("T:", t)
    # print("P%T:", p%t)
    # print("P%2:", p%2)
    # # Success

    # import numpy as np
    # A = np.array([
    #     [p],
    #     [q]
    #     ])
    # B = np.array([
    #     [r],
    #     [s]
    #     ])
    # print(A)
    # print(B)
    # C = A+B
    # print(C)
    # print(C[0][0])
    # print(C[1][0])
    # # Success

if __name__ == "__main__":
    main()
