import pickle
import streamlit as st
from pathlib import Path
import streamlit_authenticator as stauth

st.set_page_config(page_title="Login", page_icon=":bar_chart:", layout="wide")
st.title('Login')

# --- USER AUTHENTICATION ---
names = ["Administrator", "Kevin"]
usernames = ["Admin", "BimBamBoom"]

# Load Hashed passwords
file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("rb") as file:
    hashed_passwords = pickle.load(file)

# Create a dictionary for credentials
credentials = {
    'usernames': usernames,
    'names': names,
    'passwords': hashed_passwords
}

authenticate = stauth.Authenticate(names, usernames, hashed_passwords, cookie_expiry_days=30)
# Corrected import and usage

authenticate = authenticate(names, usernames, hashed_passwords, cookie_expiry_days=30)

name, authentication_status, username = authenticate.login("Login", "main")

if authentication_status == False:
    st.error("Username/password is incorrect")

if authentication_status == None:
    st.warning("Please enter your username and password")

if authentication_status:
    # ---- SIDEBAR ----
    authenticate.logout("Logout", "sidebar")
    st.sidebar.title(f"Welcome {name}")
    st.sidebar.header("Please Filter Here:")
    # ---- MAINPAGE ----
    st.title(":bar_chart: Sales Dashboard")
    st.markdown("##")
    st.markdown("""---""")

    # ---- HIDE STREAMLIT STYLE ----
    hide_st_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                header {visibility: hidden;}
                </style>
                """
    st.markdown(hide_st_style, unsafe_allow_html=True)