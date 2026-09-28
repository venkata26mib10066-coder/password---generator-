import random
import string

print("===== PASSWORD GENERATOR =====")

length = int(input("Enter password length: "))

print("\nChoose character types:")
print("1. Uppercase letters")
print("2. Lowercase letters")
print("3. Numbers")
print("4. Special characters")

choice = input("Enter your choices (example: 1234): ")

characters = ""

if "1" in choice:
    characters += string.ascii_uppercase

if "2" in choice:
    characters += string.ascii_lowercase

if "3" in choice:
    characters += string.digits

if "4" in choice:
    characters += string.punctuation

if characters == "":
    print("Please select at least one character type.")
else:
    password = ""

    for i in range(length):
        password += random.choice(characters)

    print("\nYour generated password is:")
    print(password) 
