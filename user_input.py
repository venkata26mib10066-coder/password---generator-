from validator import validate_choice


def get_password_length():
    while True:
        try:
            length = int(input("Enter password length: "))
            return length
        except ValueError:
            print("Please enter a valid number.")


def get_yes_no(prompt):
    while True:
        choice = input(prompt).strip().lower()

        if validate_choice(choice):
            return choice == "y"

        print("Please enter y or n.")