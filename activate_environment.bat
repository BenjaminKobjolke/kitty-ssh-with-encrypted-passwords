@echo off
call .\venv\Scripts\activate.bat
echo Virtual environment activated. You can now run the Python scripts.
echo.
echo Available commands:
echo - python string_crypto.py    (Store your SSH password)
echo - python launch_kitty.py     (Launch Kitty with stored password)
cmd /k
