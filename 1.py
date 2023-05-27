# Required imports
import streamlit as st
import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('data.db')
c = conn.cursor()

# Create a new table if it doesn't exist
c.execute('''
    CREATE TABLE IF NOT EXISTS user_data (
        name TEXT,
        age INTEGER
    )
''')
conn.commit()

# Get user inputs
name = st.text_input("Enter your name:")
age = st.number_input("Enter your age:", min_value=1)

if st.button("Submit"):
    # Insert the data into the database
    c.execute('''
        INSERT INTO user_data (name, age)
        VALUES (?, ?)
    ''', (name, age))
    conn.commit()

    # Display the message
    st.write(f'{name} is {age} years old.')

# Get data from the database
c.execute("SELECT * FROM user_data")
data = c.fetchall()

# Display the names and ages of all previous inputs
st.write("Previous inputs:")
for entry in data:
    st.write(f'{entry[0]} is {entry[1]} years old.')
