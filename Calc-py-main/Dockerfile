# Use an official Python runtime as the base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the entire project into the container
COPY . .

RUN pip install -r requirements.txt

# Set the entry point for the container
CMD [ "python", "calc.py"]