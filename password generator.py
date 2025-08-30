import random
import string

def generate_password(length=12, use_digits=True, use_symbols=True):
    characters = string.ascii_letters  # a-zA-Z

    if use_digits:
        characters += string.digits     # 0-9
    if use_symbols:
        characters += string.punctuation  # !@#$%^&*()...

    if length < 4:
        return "Password too short. Choose at least 4 characters."

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Example usage
print("Generated Password:", generate_password(length=16))
