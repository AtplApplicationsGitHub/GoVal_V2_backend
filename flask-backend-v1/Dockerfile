# Use an official Python runtime as a parent image
FROM python:3.13-slim

# Install libGL and libglib2.0 for OpenCV dependencies
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0

# Set the working directory in the container
WORKDIR /usr/share/app

# Copy the requirements.txt file into the container
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Make port 2053 available to the world outside this container
EXPOSE 2053

# Run the application when the container launches
CMD ["python", "wsgi.py"]
