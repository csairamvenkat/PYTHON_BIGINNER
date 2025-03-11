import random
import string

def generate_password(length=12):
    # Define the characters to choose from
    all_characters = string.ascii_letters + string.digits + string.punctuation
    
    # Randomly select characters from the list and join them into a string
    password = ''.join(random.choice(all_characters) for _ in range(length))
    
    return password

# Example usage
password = generate_password(16)  # Generates a 16-character long password
print("Generated password:", password)
