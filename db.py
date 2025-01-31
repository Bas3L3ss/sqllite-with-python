import sqlite3
import os

# Delete the existing database if it exists
if os.path.exists('customer.db'):
    os.remove('customer.db')

try:
    # Create a fresh connection
    conn = sqlite3.connect('customer.db')
    cursor = conn.cursor()

    # Create the table
    cursor.execute("""
        CREATE TABLE customers (
            first_name text,
            last_name text,
            email text
        )
    """)

    # Insert the record
    cursor.execute("INSERT INTO customers VALUES ('John', 'Elder', 'baseless@.com')")
    cursor.execute("INSERT INTO customers VALUES ('John', 'Elder', 'baseless@.com')")

    # Verify the insertion
    cursor.execute("SELECT * FROM customers")
    print("Inserted data:", cursor.fetchall())

    # Commit the changes
    conn.commit()

except sqlite3.Error as e:
    print(f"An error occurred: {e}")

finally:
    # Close the connection
    if conn:
        conn.close()