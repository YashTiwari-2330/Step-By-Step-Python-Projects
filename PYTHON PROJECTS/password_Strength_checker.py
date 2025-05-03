import re

def check_password_strength(password):
    length_error = len(password) < 8
    uppercase_error = not re.search(r"[A-Z]", password)
    lowercase_error = not re.search(r"[a-z]", password)
    digit_error = not re.search(r"[0-9]", password)
    special_char_error = not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)

    score = 5 - sum([length_error, uppercase_error, lowercase_error, digit_error, special_char_error])

    if score == 5:
        return "Strong"
    elif 3 <= score < 5:
        return "Moderate"
    else:
        return "Weak"

# Example usage
password = input("Enter your password: ")
strength = check_password_strength(password)
print(f"Password Strength: {strength}")
