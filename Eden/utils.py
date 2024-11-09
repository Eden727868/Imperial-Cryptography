from collections import Counter
from math import floor, sqrt

def string_into_columns(string: str, length: int, keyset: str) -> list[list[str]]:
    ''' Takes string, integer column length, string keyset as input, returns list of list of string as output
        Turns string into columns, eg:
        input hello world ->
        h e
        l l
        o w
        o r
        l d
        output [['h', 'l', 'o', 'o', 'l'], ['e', 'l' 'w', 'r', 'd']]
    '''
    columns = [[] for i in range(0, length)]
    current_column = 0

    for char in string:
        if char.lower() in keyset:
            columns[current_column].append(char)
            current_column += 1
            if current_column >= length:
                current_column = 0

    return columns

def most_common(lst: list):
    ''' Takes list as input, returns most common element of the list
    '''
    return max(set(lst), key=lst.count)

def is_prime(n: int) -> bool:
    ''' Takes integer as input, returns true if it is prime and false if it is not
    '''
    if n == 1:
        return False
    
    if n == 2:
        return True

    for i in range(2, floor(sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True
