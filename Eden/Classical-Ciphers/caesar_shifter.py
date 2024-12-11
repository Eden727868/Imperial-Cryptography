from englishness import get_englishness
from sys import argv

alphabet = "abcdefghijklmnopqrstuvwxyz"

def caesar_shift(plaintext: str, keyset: str, key: int) -> str:
    ''' Takes 3 paramters: plaintext, keyset (eg alphabet), key
        Returns plaintext shifted by the key
    '''
    ciphertext = ""
    number_of_keys = len(keyset)

    for char in plaintext:
        if char.lower() in keyset:
            char = char.lower()
            index = keyset.index(char)
            new_index = (index + key) % number_of_keys
            char = keyset[new_index]
            ciphertext += char
        else:
            ciphertext += char
    return ciphertext


def caesar_unshift(ciphertext: str, keyset: str, key: int) -> str:
    ''' Takes 3 parameters: ciphertext, keyset, key
        Returns the plaintext shifted in reverse by the key
    '''
    return caesar_shift(ciphertext, keyset, len(keyset) - key)


def brute_force(ciphertext: str, keyset: str) -> None:
    ''' Takes 2 parameters, ciphertext, keyset
        Tries every possible key and prints the most likely shift
    '''
    explicit = input("Explicit output? [y/n]\n")
    speed = int(input("Enter thoroughness [0, 1]\n"))

    full_list = dict()

    for current_key in range(0, len(keyset)):
        current_shift = caesar_shift(ciphertext, keyset, current_key)
        full_list[f"{current_key}: {current_shift}"] = get_englishness(current_shift, speed)

        if explicit == "y":
            print(f"{current_key}: {current_shift}", full_list[f"{current_key}: {current_shift}"])
            print("Shift key:", current_key)

    print("Maximum value:", max(full_list, key=full_list.get))

if __name__ == "__main__":
    if len(argv) != 2:
        print("Please enter 1 command-line argument: 0 to encode, 1 to decode, 2 to brute force")
        quit()

    text_input = input("Enter string\n")
    
    if argv[1] == "0":
        key = int(input("Enter key [1-26]: "))
        print(caesar_shift(string, alphabet, key))

    elif argv[1] == "1":
        key = int(input("Enter key [1-26]: "))
        print(caesar_unshift(string, alphabet, key))

    elif argv[1] == "2":
        brute_force(text_input, alphabet)