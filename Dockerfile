# Use an official Python runtime as a parent image
FROM python:3.10

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Copy the requirements file into the container at /usr/src/app
COPY requirements.txt ./

RUN apt-get update && apt-get install -y libgl1-mesa-glx

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt --timeout 500

# Make port 80 available to the world outside this container
EXPOSE 2703

ENV PYTHONPATH "${PYTHONPATH}:app"
# Run app.py when the container launches
CMD ["python", "app/main/run.py"]
