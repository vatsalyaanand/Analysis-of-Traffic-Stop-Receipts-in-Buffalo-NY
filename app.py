import streamlit as st
import psycopg2
import pandas as pd

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
            # Get column names
            colnames = [desc[0] for desc in cursor.description]

        df = pd.DataFrame(result, columns=colnames)
        st.write("Query Result:")
        st.dataframe(df)
    except Exception as e:
        st.error(f"Error executing the query: {e}")

db_connection.close()