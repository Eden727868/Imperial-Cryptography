# a program to check how many english words are in a string
def getEnglishness(string, speed):
    count = 0

    if speed == 1:
        file_path = "words_alpha.txt"
    else:
        file_path = "english_words.txt"

    with open(file_path) as file:
        words = set(file.read().split('\n'))
        string = string.split(" ")

        for word in string:
            if word.lower() in words:
                count += 1

    return float(count * 100 / len(string))

if __name__ == "__main__":
    print(getEnglishness(input("Enter a string:\n"), int(input("Enter thoroughness [0, 1]\n"))))
