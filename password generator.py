import random
import string

def generate_password(length):
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation
    all_chars = lowercase_letters + uppercase_letters + digits + special_chars
    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password

while True:
    try:
        length = int(input("Enter the desired length of the password: "))
        if length <= 0:
            raise ValueError("Length must be a positive integer.")
        elif length < 8:
            print("Password length is too short. It should be at least 8 characters.")
        elif length > 128:
            print("Password length is too long. It should be at most 128 characters.")
        else:
            break
    except ValueError as e:
        print("Invalid input. Please enter a positive integer.")

password = generate_password(length)
print("Generated Password:", password)

