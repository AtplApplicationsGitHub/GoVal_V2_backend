# Use an official Python runtime as a parent image
FROM python:3.13-slim

# Set the working directory in the container
WORKDIR /usr/share/app

# Copy the requirements.txt file into the container
COPY requirements.txt .

# Install Python dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Make port 2053 available to the outside world
EXPOSE 2053

# Run the application when the container launches
CMD ["python", "wsgi.py"]
