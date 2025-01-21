def vinegere(keyword,plain):
    cyphertext = ""
    keyword = keyword.lower()
    plain = plain.lower()
    keywordindex = 0
    keywordlength = len(keyword)
    for i in range (0, len(plain)):
        letter = keyword[keywordindex]
        if ord(plain[i]) < 97 or ord(plain[i]) > 122:
            cyphertext += plain[i]
        else:
            cyphertext += chr((((ord(plain[i])-96)+(ord(letter)-96)-1)%26)+96)
            keywordindex += 1
            keywordindex = keywordindex % keywordlength
    return cyphertext

plain = input("Please enter your plaintext")
keyword = input("Please enter your keywod to code this plaintext into cyphertext.")
print("Your cyphertext is:", vinegere(keyword,plain))



def breaker(keyword,cypher):
    keyword = keyword.lower()
    keywordindex = 0
    keywordlength = len(keyword)
    plaintext = ""
    for i in range (0, len(cypher)):
       letter = keyword[keywordindex]
       if ord(cypher[i]) < 97 or ord(cypher[i]) > 122:
            plaintext += cypher[i]
       else:
           plaintext += chr((((ord(cypher[i]) - 97) - (ord(letter) - 97) + 26) % 26) + 97)  
           keywordindex += 1
           keywordindex = keywordindex % keywordlength
    return plaintext

cypher = vinegere(keyword,plain)
print("Your plaintext was:", breaker(keyword,cypher))


