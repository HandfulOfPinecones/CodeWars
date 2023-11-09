import re

################################
# ^: Anchors the pattern to the start of the string.
# (?=.*[a-z]): Requires at least one lowercase letter.
# (?=.*[A-Z]): Requires at least one uppercase letter.
# (?=.*\d): Requires at least one digit.
# [A-Za-z\d]{6,}: Matches alphanumeric characters (letters and digits) of at least six characters in length.
# $: Anchors the pattern to the end of the string.
################################


def is_valid_password(password):
    # Define the regex pattern
    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{6,}$"

    # Check if the password matches the pattern
    if re.match(pattern, password):
        return True
    else:
        return False


# Example usage:
password = "P@ssw0rd"
if is_valid_password(password):
    print("Password is valid")
else:
    print("Password is invalid")
