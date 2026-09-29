import random
import string


def generate_password(length, use_uppercase, use_lowercase,
                      use_numbers, use_special):

    characters = ""

    if use_uppercase:
        characters += string.ascii_uppercase

    if use_lowercase:
        characters += string.ascii_lowercase

    if use_numbers:
        characters += string.digits

    if use_special:
        characters += string.punctuation

    password = ""

    for i in range(length):
        password += random.choice(characters)

    return password
