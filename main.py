from generator import generate_password
from validator import validate_length
from strength_checker import check_strength
from user_input import get_password_length, get_yes_no
from utils import display_banner, display_password


def main():
    display_banner()

    while True:

        # Get and validate password length
        length = get_password_length()

        valid, message = validate_length(length)

        if not valid:
            print(message)
            continue

        # Get character choices
        use_uppercase = get_yes_no(
            "Include uppercase letters? (y/n): "
        )

        use_lowercase = get_yes_no(
            "Include lowercase letters? (y/n): "
        )

        use_numbers = get_yes_no(
            "Include numbers? (y/n): "
        )

        use_special = get_yes_no(
            "Include special characters? (y/n): "
        )

        # Check if at least one option is selected
        if not any([
            use_uppercase,
            use_lowercase,
            use_numbers,
            use_special
        ]):
            print("Please select at least one character type.")
            continue

        # Generate password
        password = generate_password(
            length,
            use_uppercase,
            use_lowercase,
            use_numbers,
            use_special
        )

        # Display password
        display_password(password)

        # Check password strength
        print("Password Strength:", check_strength(password))

        # Ask to generate another password
        again = get_yes_no(
            "Generate another password? (y/n): "
        )

        if not again:
            print("Thank you for using the Password Generator!")
            break


if __name__ == "__main__":
    main()
