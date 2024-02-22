import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    res = re.search("src=\"https?://(?:www\.)?youtube\.com/embed/(.*?)\"", s)
    if not res:
        return None
    return(f"https://youtu.be/{res[1]}")


if __name__ == "__main__":
    main()
