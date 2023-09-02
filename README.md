
# Local Password Manager

A brief description of what this project does and who it's for


## Overview
The local password manager application enables users to securely store and manage website credentials on their local systems. It utilizes hashing and a database to protect sensitive password data.

## Implementation
The application is built using:

* Docker - Provides isolated containers to host the application * components. Ensures portability.
* PostgreSQL - Relational database to store the encrypted password entries.
* Python Flask - Backend framework to handle API requests for password operations.
* SHA-256 - Secure hashing algorithm to protect stored passwords.
## Functionality
Key features:

1. Add passwords - Users can submit website, username, password to store credentials.
2. Retrieve passwords - Users can request stored passwords by providing the website name.
## Workflow
1. User interacts with Flask API endpoints to add or retrieve passwords.
2. Passwords are hashed with SHA-256 before storage in PostgreSQL database.
3. Retrieval compares stored hash to input password hash for verification.
4. Docker containers isolate the Flask app backend and database.
## Benefits
* Increased security via hashing and local storage.
* Better portability and isolation with Docker.
* User retains full control over password data.
## Considerations
* Comprehensive security testing required before use.
* Users responsible for backup and recovery of password data.
* Graphical user interface could improve usability.
## Conclusion
The project provides a foundational local password manager using standard tools. Additional encryption, access control, and testing required to make it production-ready. 