from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64
import getpass
import subprocess

def get_key_from_password(password):
    salt = b'fixed_salt'
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
    )
    key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
    return key

def decrypt_string(encrypted_data, password):
    key = get_key_from_password(password)
    f = Fernet(key)
    decrypted_data = f.decrypt(encrypted_data)
    return decrypted_data.decode()

def main():
    try:
        # Get password securely
        password = getpass.getpass("Enter the password: ")
        
        # Read encrypted data
        with open('credentials.txt', 'rb') as f:
            encrypted_data = f.read()
        
        # Decrypt data
        decrypted_string = decrypt_string(encrypted_data, password)
        
        # Launch kitty with the decrypted password and don't wait
        subprocess.Popen(['kitty.exe', '-pass', decrypted_string, 'xida.me'])
        
    except Exception as e:
        print("Error: Invalid password or corrupted data")

if __name__ == "__main__":
    main()
