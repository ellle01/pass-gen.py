import random
import string

# user for the desired password length
password_length = int(input("Enter the desired password length: "))

# Generate a password using a mix of letters, numbers, and symbols
characters = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(characters) for i in range(password_length))
# Display the generated password
print("Generated Password:", password)
