from sys import argv

alphabet = "abcdefghijklmnopqrstuvwxyz"

def caesarShift(string, keyset, key):
    cipher = ""
    number_of_keys = len(keyset)

    for char in string:
        if char.lower() in keyset:
            char = char.lower()
            index = keyset.index(char)
            new_index = (index + key) % number_of_keys
            char = keyset[new_index]
            cipher += char
        else:
            cipher += char
    return cipher

if __name__ == "__main__":
    string = input("Enter string\n")
    
    if argv[1] == "0":

        key = int(input("Enter key [1-26]\n"))
        print(caesarShift(string, alphabet, key))

    elif argv[1] == "1":

        explicit = input("Explicit output? [y/n]\n")

        import englishness
        
        speed = int(input("Enter thoroughness [0, 1]\n"))

        full_list = dict()

        for i in range(1, 26):
            current_shift = caesarShift(string, alphabet, i)
            key = str(i) + current_shift
            full_list[f"{i}: {current_shift}"] = englishness.getEnglishness(current_shift, speed)
            if explicit == "y":
                print(f"{i}: {current_shift}", full_list[f"{i}: {current_shift}"])
                print("Shift key:", i)

        print("Maximum value:", max(full_list, key=full_list.get))
