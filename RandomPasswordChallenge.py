import random
import string
def generate_password(length):
    if length < 6:
        return "Password should be at least 6 characters long."
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    all_chars = lower + upper + digits
    password = ''.join(random.choices(all_chars, k=length))
    return password
length = int(input("Enter the password length: "))
print("Generated Password:", generate_password(length))