from functools import reduce
from collections import Counter

def kasiskiAnalyser(ciphertext: str):
    string_to_analyse = ""
    for char in ciphertext:
        if char != " ":
            string_to_analyse += char # remove spaces

    repeated_substrings = {} #substring: [positions]

    for substring_length in range(3, 12):
        for i in range(len(string_to_analyse) - substring_length - 1):
            potential_repeat = string_to_analyse[i:i+substring_length]

            positions = []
            index = 0
            while index < len(string_to_analyse):
                index = string_to_analyse.find(potential_repeat, index)
                if index == -1:
                    break
                positions.append(index)
                index += substring_length

            if len(positions) > 1 and potential_repeat not in repeated_substrings:
                if positions[0] % substring_length == positions[1] % substring_length:
                    repeated_substrings[potential_repeat] = positions

    distances = []
    for substring in repeated_substrings:
        distances.append(repeated_substrings[substring][1] - repeated_substrings[substring][0])

    distances_factors = []
    for distance in distances:
        distances_factors += factors(distance)

    distances_factors = [num for num in distances_factors if num != 1] # remove 1

    distances_factors = [item for items, c in Counter(distances_factors).most_common() for item in [items] * c] # sort into frequency

    distances_factors = list(dict.fromkeys(distances_factors)) # remove duplicates

    return distances_factors

def factors(n):
    return set(reduce(
        list.__add__,
        ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

if __name__ == "__main__":
    print(kasiskiAnalyser(input()))
