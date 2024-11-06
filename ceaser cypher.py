def ceaser(key, plain, cyphertext):
    for i in range (0, len(plain)):
        if ord(plain[i]) == 32:
            cyphertext = cyphertext + chr(32)
        elif ord(plain[i]) < 97 or ord(plain[i]) > 122:
            pass
        else:
            plain = plain.lower()
            num = ord(plain[i])
            newnum = ((num + key - 97) % 26) + 97
            cyphertext = cyphertext + chr(newnum)
    return cyphertext


cyphertext = ""                  
plain = str(input("Please enter your plaintext"))
key =  int(input("Please enter your key for your ceaser cypher"))
print("Your cyphertext is:", ceaser(key,plain,cyphertext))
cypher = ceaser(key,plain,cyphertext)



def breakceaser(cypher, keys):
            newplain = ""
            for i in range (0, len(cypher)):
               if ord(cypher[i]) == 32:
                  newplain = newplain + chr(32)
               elif ord(cypher[i]) < 97 or ord(cypher[i]) > 122:
                  pass
               else:
                  num = ord(cypher[i])
                  newnum = ((num + keys - 97) % 26) + 97
                  newplain = newplain + chr(newnum)
            return newplain      


for n in range (1,27):
    keys = n
    print("One possible solution is:", breakceaser(cypher,keys))
