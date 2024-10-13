import pickle
from pathlib import Path
import streamlit_authenticator as stauth

names = ["Administrator", "Kevin"]
usernames = ["Admin", "BimBamBoom"]
passwords = ["12345678", "12345678"]

hasher = stauth.Hasher(passwords)
hashed_passwords = [hasher.hash(password) for password in passwords]

file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("wb") as file:
    pickle.dump(hashed_passwords, file)