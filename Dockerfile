# Use the official Python image as the base image
FROM python:latest

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents to the container's working directory
COPY . /app

# Install required Python dependencies
RUN pip install psycopg2-binary

# Run the Python application
CMD [ "python", "app.py" ]