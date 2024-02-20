def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not starts_with_2_letters(s):
        return False
    elif not min_2_max_6(s):
        return False
    elif number_in_middle:
        return False
    elif first_num_0:
        return False
    elif periods_spaces_punctation_marks:
        return False
    else
        return True

# “All vanity plates must start with at least two letters.”
def starts_with_2_letters(s):
    if s[0] not in [A-Z] and s[1]
“… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
“Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
“No periods, spaces, or punctuation marks are allowed.”


main()
