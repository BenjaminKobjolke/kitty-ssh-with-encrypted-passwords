import hashlib
import getpass

def hash_string(input_string, password):
    # Combine the input string with the password as a salt
    salted_string = input_string + password
    # Create SHA-256 hash
    hasher = hashlib.sha256()
    hasher.update(salted_string.encode('utf-8'))
    return hasher.hexdigest()

def main():
    # Get input string
    input_string = input("Enter the string to hash: ")
    # Get password securely (won't be displayed while typing)
    password = getpass.getpass("Enter the password: ")
    
    # Generate hash
    hashed_result = hash_string(input_string, password)
    
    # Store in credentials.txt
    with open('credentials.txt', 'w') as f:
        f.write(hashed_result)
    
    print(f"Hash has been stored in credentials.txt")

if __name__ == "__main__":
    main()
