# Not guaranteed success, often gets close
# 0 -> encode plaintext
# 1 -> decode ciphertext with a known key
# 2 -> try and find key

from sys import argv
from englishness import *
from caesar_shifter import caesar_shift
from kasiski import kasiski_analyser
from utils import most_common, string_into_columns

alphabet = "abcdefghijklmnopqrstuvwxyz"

def vigenere_cipher(plaintext: str, keyword: str) -> str:
    ''' Takes string plaintext, string keyword as inputs, returns string ciphertext
    '''

    ciphertext = ""
    current_cipher_index = 0
    length_of_keyword = len(keyword)

    for char in plaintext:
        if char.lower() in alphabet:
            if current_cipher_index > length_of_keyword - 1:
                current_cipher_index = 0
            local_key = alphabet.index(keyword[current_cipher_index].lower())
            ciphertext += caesar_shift(char, alphabet, local_key)
            current_cipher_index += 1
        else:
            ciphertext += char

    return ciphertext

def vigenere_decipher(ciphertext: str, keyword: str):
    ''' Takes string ciphertext, string keyword, returns plaintext
        Only used if the keyword is known
    '''

    plaintext = ""
    current_plain_index = 0
    length_of_keyword = len(keyword)

    for char in ciphertext:
        if char.lower() in alphabet:
            if current_plain_index > length_of_keyword - 1:
                current_plain_index = 0
            local_key = 26 - alphabet.index(keyword[current_plain_index].lower())
            plaintext += caesar_shift(char, alphabet, local_key)
            current_plain_index += 1
        else:
            plaintext += char

    return plaintext

def vigenere_solve(ciphertext: str) -> None:
    ''' Method that only takes string ciphertext as input, returns no value
        Runs kasiski analysis on ciphertext to guess keylength, then uses frequency analysis to guess keyword
    '''
    likely_keylengths = kasiski_analyser(ciphertext)
    likely_keylengths = [num for num in likely_keylengths if num <= 10]
    print(likely_keylengths)

    keys = []

    for length in likely_keylengths:
        columns = string_into_columns(ciphertext, length, alphabet)
        key = ""

        for column in columns:
            most_common_letter = most_common(column)
            index = alphabet.index(most_common_letter.lower()) - 4 #index of e
            key += alphabet[index]
        
        keys.append(key)

    key_chart = {} #[key, plaintext]: probability

    for key in keys:
        potential_plaintext = vigenere_decipher(ciphertext, key)
        print(potential_plaintext)
        probability = get_englishness(potential_plaintext, 1)

        key_chart[key, potential_plaintext] = probability

    best_guess = max(key_chart, key = lambda x: key_chart[x])
    print("----------\nBest guess:\nKey:", best_guess[0], "\nPlaintext:", best_guess[1])

if __name__ == "__main__":
    if len(argv) != 2:
        print("Please enter a command-line argument: 0 to encode, 1 to decode with a known key, 2 to solve the key")
        quit()
    if argv[1] == "0":
        plaintext = input("Enter a string\n")
        key = input("Enter a key\n")
        print(vigenere_cipher(plaintext, key))
    elif argv[1] == "1":
        ciphertext = input("Enter a string\n")
        key = input("Enter a key\n")
        print(vigenere_decipher(ciphertext, key))
    elif argv[1] == "2":
        ciphertext = input("Enter a string\n")
        vigenere_solve(ciphertext)
