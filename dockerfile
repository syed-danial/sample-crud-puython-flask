# Use an official Python runtime as the base image
FROM python:3.8

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

RUN apt-get update && \
    apt-get install -y libpq-dev gcc && \
    pip install --no-cache-dir flask psycopg2-binary

# Install any needed dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt


# Copy the current directory contents into the container at /app
COPY . /app

# Expose the port your app runs on
EXPOSE 5000

# Define the command to run your application
CMD ["python3", "app.py"]
