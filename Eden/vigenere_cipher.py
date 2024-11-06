# Not guaranteed success, often gets close
# 0 -> encode plaintext
# 1 -> decode ciphertext with a known key
# 2 -> try and find key

from sys import argv
from englishness import *
import caesar_shifter
import kasiski
import utils

alphabet = "abcdefghijklmnopqrstuvwxyz"

def vigenereCipher(string: str, keyword: str):

    ciphertext = ""
    current_cipher_index = 0
    length_of_keyword = len(keyword)

    for char in string:
        if char.lower() in alphabet:
            if current_cipher_index > length_of_keyword - 1:
                current_cipher_index = 0
            local_key = alphabet.index(keyword[current_cipher_index].lower())
            ciphertext += caesar_shifter.caesarShift(char, alphabet, local_key)
            current_cipher_index += 1
        else:
            ciphertext += char

    return ciphertext

def vigenereDecipher(string: str, keyword: str):

    plaintext = ""
    current_plain_index = 0
    length_of_keyword = len(keyword)

    for char in string:
        if char.lower() in alphabet:
            if current_plain_index > length_of_keyword - 1:
                current_plain_index = 0
            local_key = 26 - alphabet.index(keyword[current_plain_index].lower())
            plaintext += caesar_shifter.caesarShift(char, alphabet, local_key)
            current_plain_index += 1
        else:
            plaintext += char

    return plaintext

def vigenereSolve(ciphertext: str):
    likely_keylengths = kasiski.kasiskiAnalyser(ciphertext)
    likely_keylengths = [num for num in likely_keylengths if num <= 10]
    print(likely_keylengths)

    keys = []

    for length in likely_keylengths:
        columns = utils.stringIntoColumns(ciphertext, length, alphabet)
        key = ""

        for column in columns:
            most_common_letter = utils.most_common(column)
            index = alphabet.index(most_common_letter.lower()) - 4 #index of e
            key += alphabet[index]
        
        keys.append(key)

    key_chart = {} #[key, plaintext]: probability

    for key in keys:
        potential_plaintext = vigenereDecipher(ciphertext, key)
        print(potential_plaintext)
        probability = getEnglishness(potential_plaintext, 1)

        key_chart[key, potential_plaintext] = probability

    best_guess = max(key_chart, key = lambda x: key_chart[x])
    print("----------\nBest guess:\nKey:", best_guess[0], "\nPlaintext:", best_guess[1])

if __name__ == "__main__":
    if argv[1] == "0":
        plaintext = input("Enter a string\n")
        key = input("Enter a key\n")
        print(vigenereCipher(plaintext, key))
    elif argv[1] == "1":
        ciphertext = input("Enter a string\n")
        key = input("Enter a key\n")
        print(vigenereDecipher(ciphertext, key))
    elif argv[1] == "2":
        ciphertext = input("Enter a string\n")
        vigenereSolve(ciphertext)
