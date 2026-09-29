def check_strength(password):
    score = 0

    if len(password) >= 8:
        score += 1

    has_uppercase = False
    has_lowercase = False
    has_number = False
    has_special = False

    for character in password:
        if character.isupper():
            has_uppercase = True
        elif character.islower():
            has_lowercase = True
        elif character.isdigit():
            has_number = True
        else:
            has_special = True

    if has_uppercase:
        score += 1

    if has_lowercase:
        score += 1

    if has_number:
        score += 1

    if has_special:
        score += 1

    if score <= 2:
        return "Weak"
    elif score <= 4:
        return "Medium"
    else:
        return "Strong"
