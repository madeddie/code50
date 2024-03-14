def main():
    st = input("Input:")
    print("Output:", end="")
    print(shorten(st))

def shorten(word):
    word = word.strip()
    output = ""
    for c in word:
        if c in "AEIOUaeiou":
            c = ""
        output += c
    return output

if __name__ == "__main__":
    main()
