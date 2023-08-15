# # Use an official Python runtime as the base image
# FROM python:3.9

# # Set the working directory in the container to /app
# WORKDIR /app

# # Copy the contents of the mlproject directory into the container at /app
# COPY ../ /app

# # Install the required packages
# RUN pip install --no-cache-dir -r requirements.txt

# # Make port 5000 available to the world outside this container
# EXPOSE 5000

# # Run application.py when the container launches
# CMD ["python", "application.py"]

######################################################################
# Docker for AWS

# Use an official Python runtime as the base image
FROM python:3.9

# Set the working directory in the container to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Run application.py when the container launches
CMD ["python", "application.py"]
