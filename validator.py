def validate_length(length):
    if length < 4:
        print("Password length should be at least 4.")
        return False

    if length > 100:
        print("Password length should not exceed 100.")
        return False

    return True


def check_character_selection(uppercase, lowercase, numbers, special):
    if not (uppercase or lowercase or numbers or special):
        print("Please select at least one character type.")
        return False

    return True


def validate_password_length(length):
    try:
        length = int(length)

        if validate_length(length):
            print("Password length is valid.")
            return True
        else:
            return False

    except ValueError:
        print("Please enter a valid number.")
        return False