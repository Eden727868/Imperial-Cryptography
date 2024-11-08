# a program to check how many english words are in a string
def get_englishness(text, speed):
    count = 0

    if speed == 1:
        words_list_file = "words_alpha.txt"
    else:
        words_list_file = "english_words.txt"

    with open(words_list_file) as words_list_file:
        words = set(words_list_file.read().split('\n'))
        text = text.split(" ")

        for word in text:
            if word.lower() in words:
                count += 1

    return float(count * 100 / len(text))

if __name__ == "__main__":
    print(get_englishness(input("Enter a string:\n"), int(input("Enter thoroughness [0, 1]\n"))))
