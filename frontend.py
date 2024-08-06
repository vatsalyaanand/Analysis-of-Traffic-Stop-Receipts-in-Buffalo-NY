import streamlit as st
import psycopg2

# Database connection
db_connection = psycopg2.connect(
    dbname="CSE 4/560 Project",
    user="postgres",
    password="vatsalya",
    host="localhost",
    port="5433"
)

# Streamlit app
st.title("Database Viewer")

# Input for SQL query
query = st.text_area("Enter your SQL query")

# Button to execute the query
if st.button("Run Query"):
    try:
        # Execute the query
        with db_connection.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()

        # Display the result
        st.write("Query Result:")
        st.write(result)
    except Exception as e:
        st.error(f"Error executing the query: {e}")

# Close the database connection
db_connection.close()