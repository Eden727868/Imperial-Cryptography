def get_ioc(keyset, text):
    ioc = float(0)
    text = [char.lower() for char in text if char.lower() in keyset] # methods applied can be changed to suit the problem
    length = len(text)
    for char in keyset:
        occurences = text.count(char)
        probability = float( (occurences / length) * ((occurences-1) / (length-1)) )
        ioc += probability
    return ioc

if __name__ == "__main__":
    print(get_ioc("abcdefghijklmnopqrstuvwxyz", input().lower()))
