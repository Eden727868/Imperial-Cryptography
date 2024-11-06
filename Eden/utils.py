from collections import Counter

def stringIntoColumns(string: str, length: int, alphabet: str):
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
