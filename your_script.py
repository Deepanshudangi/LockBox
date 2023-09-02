# Import the necessary modules
import app

# Storing a new password
app.store_password("example_service", "example_user", "example_password")

# Retrieving a password
retrieved_password = app.retrieve_password("example_service")

# Check if the password was found and print the results
if retrieved_password:
    print("Username:", retrieved_password[0])
    print("Password:", retrieved_password[1])
else:
    print("Service not found in the password manager.")