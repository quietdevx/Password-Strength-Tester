import random

letters = list("abcdefghijklmnopqrstuvwxyz")
numbers = list("0123456789")
symbols = list("!@#$%^&*()_+-=[]{}|;:,.<>?")

def generate_strong_password():
    characters = letters + numbers + symbols
    password = ""
    for _ in range(12):  # Generate 12 character strong password
        password += random.choice(characters)
    return password

strength = 0
askforpassword = input("Enter a password: ").strip()
passwordlength = len(askforpassword)
uppercase = any(char.isupper() for char in askforpassword)
lowercase = any(char.islower() for char in askforpassword)
digits = any(char.isdigit() for char in askforpassword)
special = any(char in "!@#$%^&*()_+-=[]{}|;:,.<>?" for char in askforpassword)

if passwordlength >= 8:
    strength += 1
if uppercase:
    strength += 1
if lowercase:
    strength += 1
if digits:
    strength += 1
if special:
    strength += 1

if strength <= 2:
    print("You have a weak password")
    print("Here's a stronger password for you:", generate_strong_password())
elif strength <= 4:
    print("You have a medium password")
    print("Here's a stronger password for you:", generate_strong_password())
else:
    print("You have a strong password")
