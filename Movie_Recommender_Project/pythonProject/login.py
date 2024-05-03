import streamlit as st
import sqlite3
import hashlib


def main():
    st.header("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        # Hash the provided password for comparison
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        # Query the database for the user's credentials
        cursor.execute('SELECT * FROM Register_Users WHERE username = ?', (username,))
        user = cursor.fetchone()

        if user and user[2] == hashed_password:
            return True  # Authentication successful
        else:
            return False  # Authentication failed
