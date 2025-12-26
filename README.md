# Kitty SSH Helper for Windows

A helper tool for Kitty SSH with secure password encryption.

## Prerequisites

- Python must be installed

## Installation

Run `install.bat` to set up the environment.

## Setup

1. Launch `kitty.exe`
2. Configure your SSH settings (host, username, port, etc.)
3. Save the session as "my-server" (and as "Default Settings")
4. Close Kitty

## Store Your Password

1. Run `activate_environment.bat` to activate the Python environment
2. Run the encryption tool:
   ```
   python string_crypto.py
   ```
3. Choose option 1 to encrypt a string
4. Enter your SSH password when prompted
5. Enter an encryption password (used to decrypt your SSH password later)

## Connecting

1. Run `start_kitty.bat`
2. Enter your encryption password when prompted
3. The script will automatically connect to your SSH server

## Security Notes

- Your SSH password is stored encrypted in `credentials.txt`
- The encryption password is never stored
- Always keep your encryption password secure
