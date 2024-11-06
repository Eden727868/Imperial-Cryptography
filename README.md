# Imperial Cryptography Project

## Eden's files

### Ciphers

#### caesar_shifter.py

- To encode a string, use command line argument '0'
- To decode a string via brute force, use command line argument '1'

#### vigenere_cipher.py
- To encode a string, use command line argument '0'
- To decode a string with a known key, use command line argument '1'
- To guess the key of a ciphertext, use command line argument '2' <br>
**the key guesser is not perfect, but tends to work better with larger ciphertexts**

---

### Helpers

#### englishness.py
A program to estimate probability that a given text is the correct plaintext.
It reads from 1 of 2 lists of english words, with english_words.txt only being common words and words_alpha.txt being a much larger set of words

#### ioc.py
- A program to calculate the Index of Coincidence of a given string
- The Index of Coincidence is the probability that any 2 characters in the string are the same character
- The average English index of coincidence is 1.7

#### kasiski.py
A program for vigenere_cipher.py to guess the length of the keyword, using kasiski analysis
[Kasiski analysis taken from here](https://pages.mtu.edu/~shene/NSF-4/Tutorial/VIG/Vig-Kasiski.html)

#### utils.py
A program with functions that are likely to be used by many other programs, like finding the most common letter
