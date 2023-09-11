# Use an official Python runtime as a parent image
FROM python:3.10

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the requirements file into the container at /usr/src/app
COPY requirements.txt ./
# Install CMake
RUN apt-get update && apt-get install -y cmake
# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the local app directory contents into the container at /usr/src/app
COPY ./app ./app

# Expose the port the app runs on
EXPOSE 5000

# Define environment variable for config file path
ENV CONFIG_PATH=main/config/config.ini

# Run app.py when the container launches
CMD ["python", "app/main/run.py"]
