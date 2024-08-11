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

# Streamlit app with tabs
st.title("Database Viewer")

# Tabs for navigation
tab1, tab2 = st.tabs(["Sample Queries", "Custom Query"])

with tab1:
    st.subheader("Sample Queries")

    # Query 1
    st.subheader("Query 1")
    st.write("**The average age and the number of traffic stops grouped by race**")
    predefined_query = """
    SELECT Person.Race,
    ROUND(AVG(Person.Age), 2) AS AvgAge,
    COUNT(*) AS StopCount
    FROM Person
    JOIN TrafficStop ON
    Person.Person_ID = TrafficStop.Person_ID
    GROUP BY Person.Race
    ORDER BY StopCount DESC;
    """

    # Toggle button to show/hide the query
    with st.expander("Show Query"):
        st.code(predefined_query, language="sql")

    # Automatically run the predefined query
    try:
        with db_connection.cursor() as cursor:
            cursor.execute(predefined_query)
            result = cursor.fetchall()
            # Get column names
            colnames = [desc[0] for desc in cursor.description]

        df = pd.DataFrame(result, columns=colnames)
        st.write("Result:")
        st.dataframe(df)
    except Exception as e:
        st.error(f"Error executing Query 1: {e}")

    # Query 2
    st.subheader("Query 2")
    st.write("**Persons involved in traffic stops who are older than the average age**")
    query2 = """
    SELECT Person_ID, Race, Age, Sex, Ethnicity
    FROM Person
    WHERE Age > (SELECT AVG(Age) FROM PERSON);
    """

    # Toggle button to show/hide the query
    with st.expander("Show Query"):
        st.code(query2, language="sql")

    # Automatically run Query 2
    try:
        with db_connection.cursor() as cursor:
            cursor.execute(query2)
            result = cursor.fetchall()
            # Get column names
            colnames = [desc[0] for desc in cursor.description]

        df = pd.DataFrame(result, columns=colnames)
        st.write("Result:")
        st.dataframe(df)
    except Exception as e:
        st.error(f"Error executing Query 2: {e}")

    # Query 3
    st.subheader("Query 3")
    st.write("**Top 5 locations (addresses) with the highest number of traffic stops**")
    query3 = """
    SELECT Location.Address, Location.ZipCode,
    Location.Neighborhood,
    Location.PoliceDistrict,
    COUNT(*) as StopCount
    FROM TrafficStop
    JOIN Location ON
    TrafficStop.Latitude =
    Location.Latitude
    AND TrafficStop.Longitude =
    Location.Longitude
    GROUP BY Location.Address,
    Location.ZipCode,
    Location.Neighborhood,
    Location.PoliceDistrict
    ORDER BY StopCount DESC
    LIMIT 5;
    """

    # Toggle button to show/hide the query
    with st.expander("Show Query"):
        st.code(query3, language="sql")

    # Automatically run Query 3
    try:
        with db_connection.cursor() as cursor:
            cursor.execute(query3)
            result = cursor.fetchall()
            # Get column names
            colnames = [desc[0] for desc in cursor.description]

        df = pd.DataFrame(result, columns=colnames)
        st.write("Result:")
        st.dataframe(df)
    except Exception as e:
        st.error(f"Error executing Query 3: {e}")

    # Query 4
    st.subheader("Query 4")
    st.write("**The locations (addresses and neighborhoods) where "
             "traffic stops without body cameras were issued on weekends**")
    query4 = """
    SELECT Location.Address, Location.Neighborhood
    FROM TrafficStop
    JOIN Location ON
    TrafficStop.Latitude
    = Location.Latitude
    AND TrafficStop.Longitude
    = Location.Longitude
    WHERE TrafficStop.BodyCam = FALSE
    AND (TrafficStop.DayOfWeek = 'SATURDAY'
    OR TrafficStop.DayOfWeek = 'SUNDAY')
    GROUP BY Location.Neighborhood, Location.Address;
    """

    # Toggle button to show/hide the query
    with st.expander("Show Query"):
        st.code(query4, language="sql")

    # Automatically run Query 4
    try:
        with db_connection.cursor() as cursor:
            cursor.execute(query4)
            result = cursor.fetchall()
            # Get column names
            colnames = [desc[0] for desc in cursor.description]

        df = pd.DataFrame(result, columns=colnames)
        st.write("Result:")
        st.dataframe(df)
    except Exception as e:
        st.error(f"Error executing Query 4: {e}")

with tab2:
    st.subheader("Custom Query")

    # Input for custom SQL query
    query = st.text_area("Enter your SQL query")

    # Button to execute the custom query
    if st.button("Run Custom Query"):
        try:
            with db_connection.cursor() as cursor:
                cursor.execute(query)
                result = cursor.fetchall()
                # Get column names
                colnames = [desc[0] for desc in cursor.description]

            df = pd.DataFrame(result, columns=colnames)
            st.write("Custom Query Result:")
            st.dataframe(df)
        except Exception as e:
            st.error(f"Error executing the query: {e}")

db_connection.close()
