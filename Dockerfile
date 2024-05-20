# Use an official Python runtime as a parent image
FROM python:3.11-alpine

# Define environment variables
ENV HOST 0.0.0.0
ENV PORT 8231
ENV BASE_URL http://{HOST}:{PORT}

# Set the working directory in the container to /app
WORKDIR /app

# Add the current directory contents into the container at /app
ADD . /app

RUN apk update

RUN apk add ffmpeg git curl

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt


EXPOSE 8231

# Run the command to start uWSGI
CMD ["python3", "main.py"]
