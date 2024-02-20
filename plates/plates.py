def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not starts_with_2_letters(s):
        print("starts")
        return False
    elif not min_2_max_6(s):
        print("minmax")
        return False
    elif number_in_middle(s):
        print("middle")
        return False
    elif first_num_0(s):
        print("first")
        return False
    elif periods_spaces_punctation_marks(s):
        print("punct")
        return False
    else:
        return True

# “All vanity plates must start with at least two letters.”
def starts_with_2_letters(s):
    return s[0:2].isalpha()

# “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
def min_2_max_6(s):
    return 6 >= len(s) >= 2

# “Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
def number_in_middle(s):
    found_digit = False
    for char in s:
        print(char)
        if char.isdigit():
            found_digit = True
        elif char.isalpha() and found_digit:
            return True
        return False

def first_num_0(s):
    for char in s:
        if char.isdigit():
            return char == "0"

# “No periods, spaces, or punctuation marks are allowed.”
def periods_spaces_punctation_marks(s):
    return not s.isalnum()

main()
