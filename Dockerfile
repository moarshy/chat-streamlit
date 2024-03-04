# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file into the container at /app
COPY requirements.txt /app/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Install Streamlit specifically
RUN pip install streamlit

# Copy the rest of your app's source code from your host to your image filesystem.
COPY . /app

# Make port 8003 available to the world outside this container
EXPOSE 8003

# Define environment variable
ENV STREAMLIT_SERVER_PORT 8003

# Run Streamlit when the container launches
CMD ["streamlit", "run", "main.py", "--server.port=8003"]