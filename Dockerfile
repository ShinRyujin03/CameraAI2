# Use an official Python runtime as a parent image
FROM python:3.10

# Set the working directory in the container
WORKDIR app

# Copy the requirements file into the container at /usr/src/app
COPY requirements.txt ./
# Install CMake
RUN apt-get update && apt-get install -y cmake
RUN apt-get update && apt-get install -y libgl1-mesa-glx

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt --timeout 500

# Copy the configuration file
COPY app/config.ini/ .
# Copy the rest of the application files
COPY . .

ENV PYTHONPATH "${PYTHONPATH}:app"
# Run app.py when the container launches
CMD ["python", "app/main/run.py"]
