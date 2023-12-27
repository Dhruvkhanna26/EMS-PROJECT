import mysql.connector

# Connect to the MySQL server
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Dhruvson@2602',
    database='stud_info'
)

# Create a cursor
cursor = conn.cursor()

try:
    # Execute a sample query (replace this with your actual query)
    query = "SELECT * FROM students"
    cursor.execute(query)

    # Fetch all the rows
    rows = cursor.fetchall()

    # Print the results
    for row in rows:
        print(row)

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    # Close the cursor and connection
    cursor.close()
    conn.close()
