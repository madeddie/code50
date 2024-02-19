def convert(input_str):
    return input_str.replace(":)", "🙂").replace(":(", "🙁")

def main():
    prompt = input("emojify me: ")
    print(convert(prompt))

main()
