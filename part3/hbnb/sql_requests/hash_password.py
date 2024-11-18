#!/usr/bin/python3
import bcrypt

password = "admin1234"
hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
print(f"Hashed Password: {hashed_password}")
