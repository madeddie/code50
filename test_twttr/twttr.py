def main():
    devowel = input("You hate vowels where? ").strip()
    print(shorten(devowel))


def shorten(word):
    for char in ["A", "E", "I", "O", "U"]:
        word = word.replace(char, "")
        word = word.replace(char.lower(), "")

    return word

if __name__ == "__main__":
    main()
