# Start with the python base image from Docker Hub
FROM python:3.9-slim-buster

WORKDIR /src

# Create python-app directory
COPY ./requirements.txt /src/requirements.txt

# Install the dependencies 
RUN pip install -r requirements.txt

# Expose the port the server runs on
EXPOSE 5000

COPY . /src

# Define a default command to start the server
CMD ["python", "findings.py"]