import streamlit as st
import sqlite3
import hashlib

def main():
    st.header("Register")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    email = st.text_input("Email")
    if st.button("Register"):
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Register_Users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                Username TEXT UNIQUE,
                Password TEXT,
                Email TEXT
            )
        ''')
        conn.commit()
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        # Insert the user credentials into the database
        try:
            cursor.execute('INSERT INTO Register_Users (Username, Password, Email) VALUES (?, ?, ?)', (username, hashed_password,email))
            conn.commit()
            return True  # Registration successful
        except sqlite3.IntegrityError:
            return False  # Username already exists