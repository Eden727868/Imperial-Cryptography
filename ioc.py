def getIOC(keyset, string):
    ioc = float(0)
    string = [char.lower() for char in string if char.lower() in keyset] # methods applied can be changed to suit the problem
    length = len(string)
    for char in keyset:
        occurences = string.count(char)
        probability = float( (occurences / length) * ((occurences-1) / (length-1)) )
        ioc += probability
    return ioc * 26

if __name__ == "__main__":
    print(getIOC("abcdefghijklmnopqrstuvwxyz", input().lower()))
