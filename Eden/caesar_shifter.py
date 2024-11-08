import englishness
from sys import argv

alphabet = "abcdefghijklmnopqrstuvwxyz"

def caesar_shift(plaintext, keyset, key):
    cipher = ""
    number_of_keys = len(keyset)

    for char in plaintext:
        if char.lower() in keyset:
            char = char.lower()
            index = keyset.index(char)
            new_index = (index + key) % number_of_keys
            char = keyset[new_index]
            cipher += char
        else:
            cipher += char
    return cipher

def caesar_unshift(ciphertext, keyset, key):
    return caesar_shift(ciphertext, keyset, len(keyset) - key)

if __name__ == "__main__":
    if len(argv) != 2:
        print("Please enter 1 command-line argument: 0 to encode, 1 to decode")
        quit()

    text_input = input("Enter string\n")
    
    if argv[1] == "0":

        key = int(input("Enter key [1-26]\n"))
        print(caesar_shift(string, alphabet, key))

    elif argv[1] == "1":

        key = int(input("Enter key [1-26, or 0 to brute force]\n"))

        if key == 0:

            explicit = input("Explicit output? [y/n]\n")
            speed = int(input("Enter thoroughness [0, 1]\n"))

            full_list = dict()

            for i in range(1, len(alphabet)):
                current_shift = caesar_shift(string, alphabet, i)
                key = str(i) + current_shift
                full_list[f"{i}: {current_shift}"] = englishness.get_englishness(current_shift, speed)
                if explicit == "y":
                    print(f"{i}: {current_shift}", full_list[f"{i}: {current_shift}"])
                    print("Shift key:", i)

            print("Maximum value:", max(full_list, key=full_list.get))

        else:
            print(caesar_unshift(string, alphabet, key))
