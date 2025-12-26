from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64
import getpass
import os

def get_key_from_password(password):
    # Use PBKDF2 to derive a key from the password
    salt = b'fixed_salt'  # In production, use a random salt and store it
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
    )
    key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
    return key

def encrypt_string(input_string, password):
    # Generate key from password
    key = get_key_from_password(password)
    # Create Fernet cipher
    f = Fernet(key)
    # Encrypt the string
    encrypted_data = f.encrypt(input_string.encode())
    return encrypted_data

def decrypt_string(encrypted_data, password):
    # Generate key from password
    key = get_key_from_password(password)
    # Create Fernet cipher
    f = Fernet(key)
    # Decrypt the data
    decrypted_data = f.decrypt(encrypted_data)
    return decrypted_data.decode()

def encrypt_and_save():
    # Get input string
    input_string = input("Enter the string to encrypt: ")
    # Get password securely
    password = getpass.getpass("Enter the password: ")
    
    # Encrypt string
    encrypted_data = encrypt_string(input_string, password)
    
    # Store in credentials.txt
    with open('credentials.txt', 'wb') as f:
        f.write(encrypted_data)
    
    print("Encrypted string has been stored in credentials.txt")

def decrypt_and_show():
    # Get password securely
    password = getpass.getpass("Enter the password: ")
    
    try:
        # Read encrypted data
        with open('credentials.txt', 'rb') as f:
            encrypted_data = f.read()
        
        # Decrypt data
        decrypted_string = decrypt_string(encrypted_data, password)
        print(f"Decrypted string: {decrypted_string}")
    except Exception as e:
        print("Error: Invalid password or corrupted data")

def main():
    while True:
        print("\nChoose an option:")
        print("1. Encrypt a string")
        print("2. Decrypt stored string")
        print("3. Exit")
        
        choice = input("Enter your choice (1-3): ")
        
        if choice == '1':
            encrypt_and_save()
        elif choice == '2':
            decrypt_and_show()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
