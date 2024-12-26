from itertools import zip_longest

class Polynomial:
    def __init__(self, coefficients: list[int]) -> None:
        ''' Coefficients are of descending order of degree (x^3, x, x^2, ...)
        '''
        self.coefficients = coefficients

    def get_degree(self) -> int:
        ''' Returns the degree of the polynomial (the max power)
        '''
        return len(self.coefficients)-1

    def clean(self) -> None:
        ''' Removes leading zeros in polynomial coefficients
        '''
        try:
            while self.coefficients[0] == 0:
                del self.coefficients[0]
        except:
            self.coefficients = []

    def __add__(self, other) -> 'Polynomial':
        ''' Adds polynomials
        '''
        coefficients = [x+y for x,y in zip_longest(reversed(self.coefficients), reversed(other.coefficients), fillvalue=0)][::-1]
        output = Polynomial(coefficients)
        output.clean()
        return output

    def __sub__(self, other) -> 'Polynomial':
        ''' Subtracts polynomials
        '''
        coefficients = [x-y for x,y in zip_longest(reversed(self.coefficients), reversed(other.coefficients), fillvalue=0)][::-1]
        output = Polynomial(coefficients)
        output.clean()
        return output

    def __mul__(self, other) -> 'Polynomial':
        ''' Used for both integer * polynomial and polynomial * polynomial
        '''
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
        ''' Floor divides each coefficient in self.coefficients by 'other'
        '''
        coefficients = [n // other for n in self.coefficients]
        return Polynomial(coefficients)

    def __mod__(self, other) -> 'Polynomial':
        ''' Takes the polynomial or integer modulus of a polynomial
            For kyber, it is only necessary to take mod (x^n + 1), so this has not been tested for polynomials not of this form.
            If 'other' is an int, then each coefficient in self.coefficients is taken mod other
        '''
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
        ''' Outputs polynomial in readable form
        '''
        out = ""

        for i in range(self.get_degree()):
            current_power = self.get_degree() - i
            out += str(self.coefficients[i]) + "x^" + str(current_power) + " + "
        out += str(self.coefficients[-1])

        return out
