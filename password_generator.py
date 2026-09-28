import string
import secrets
import math


print("===================================")
print("     RANDOM PASSWORD GENERATOR")
print("===================================")

# Character sets
letters = string.ascii_letters
digits = string.digits
symbols = string.punctuation

# All characters that can be used in the password
characters = letters + digits + symbols


# Taking password length from the user
while True:
    try:
        length = int(input("Enter password length: "))

        if length < 8:
            print("Password should be at least 8 characters long.")
        else:
            break

    except ValueError:
        print("Please enter a valid number.")


# Generating the password
password = []

for i in range(length):
    character = secrets.choice(characters)
    password.append(character)

# Joining all characters into one password
password = "".join(password)


# Calculating password entropy
character_pool_size = len(characters)
entropy = length * math.log2(character_pool_size)


# Displaying the result
print("\n-----------------------------------")
print("Generated Password:", password)
print("Password Length:", length)
print("Character Pool:", character_pool_size)
print("Estimated Entropy: {:.2f} bits".format(entropy))
print("-----------------------------------")

print("Password generated successfully!")