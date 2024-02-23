from validator_collection import checkers


email = input("What's your email address? ").strip()

if checkers.is_email(email):
    print('Valid')
else:
    print('Invalid')
