import re


def check_password_strength(password):
    """Assess the strength of a password."""
    length_criteria = len(password) >= 8
    lowercase_criteria = re.search(r"[a-z]", password) is not None
    uppercase_criteria = re.search(r"[A-Z]", password) is not None
    number_criteria = re.search(r"\d", password) is not None
    special_character_criteria = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is not None

    criteria_met = sum(
        [length_criteria, lowercase_criteria, uppercase_criteria, number_criteria, special_character_criteria])

    if criteria_met == 5:
        strength = "Very Strong"
    elif criteria_met == 4:
        strength = "Strong"
    elif criteria_met == 3:
        strength = "Moderate"
    elif criteria_met == 2:
        strength = "Weak"
    else:
        strength = "Very Weak"

    feedback = []
    if not length_criteria:
        feedback.append("Password should be at least 8 characters long.")
    if not lowercase_criteria:
        feedback.append("Password should include lowercase letters.")
    if not uppercase_criteria:
        feedback.append("Password should include uppercase letters.")
    if not number_criteria:
        feedback.append("Password should include numbers.")
    if not special_character_criteria:
        feedback.append("Password should include special characters (e.g., !@#$%^&*()).")

    return strength, feedback


def main():
    print("Welcome to the Password Strength Checker")
    print("This tool was created by Ikramul Molla.")
    print()

    while True:
        password = input("Enter a password to check its strength (or type 'Q' to quit): ")
        if password.upper() == 'Q':
            break

        strength, feedback = check_password_strength(password)
        print(f"Password Strength: {strength}")

        if feedback:
            print("Feedback:")
            for tip in feedback:
                print(f"- {tip}")
        else:
            print("Great password!")


if __name__ == "__main__":
    main()
