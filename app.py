# Import required modules
import psycopg2

# Function to store a new password
def store_password(service, username, password):
    conn = psycopg2.connect(
        dbname="password_manager_db",
        user="password_manager_user",
        password="mysecretpassword",
        host="localhost",
        port="5432"
    )
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO passwords (service, username, password) VALUES (%s, %s, %s)",
        (service, username, password)
    )
    conn.commit()
    conn.close()

# Function to retrieve a password
def retrieve_password(service):
    conn = psycopg2.connect(
        dbname="password_manager_db",
        user="password_manager_user",
        password="mysecretpassword",
        host="localhost",
        port="5432"
    )
    cursor = conn.cursor()
    cursor.execute(
        "SELECT username, password FROM passwords WHERE service = %s",
        (service,)
    )
    result = cursor.fetchone()
    conn.close()
    return result

# Example usage
if __name__ == "__main__":
    store_password("example_service", "example_user", "example_password")
    retrieved_password = retrieve_password("example_service")
    print("Username:", retrieved_password[0])
    print("Password:", retrieved_password[1])
