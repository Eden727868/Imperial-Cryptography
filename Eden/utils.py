from collections import Counter
from math import floor, sqrt

def string_into_columns(string: str, length: int, alphabet: str):
    columns = [[] for i in range(0, length)]
    current_column = 0

    for char in string:
        if char.lower() in alphabet:
            columns[current_column].append(char)
            current_column += 1
            if current_column >= length:
                current_column = 0

    return columns

def most_common(lst):
    return max(set(lst), key=lst.count)

def is_prime(n: int) -> bool:
    if n == 1:
        return False
    
    if n == 2:
        return True

    for i in range(2, floor(sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True
