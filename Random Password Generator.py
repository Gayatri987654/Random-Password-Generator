import random
import string

def generate_password(length=12):
    """
    Generate a random password of a given length.
    """
    # Define the character set for the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate the password randomly
    password = ''.join(random.choice(characters) for i in range(length))
    
    return password

def main():
    # Get the desired length of the password from the user
    length = int(input("Enter the length of the password: "))
    
    # Generate the password
    password = generate_password(length)
    
    # Display the generated password
    print("Generated Password:", password)

if __name__ == "__main__":
    main()
