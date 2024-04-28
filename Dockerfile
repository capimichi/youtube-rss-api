# Use an official Python runtime as a parent image
FROM python:3.11

# Define environment variables
ENV HOST 0.0.0.0
ENV PORT 80
ENV BASE_URL http://{HOST}:{PORT}

# Set the working directory in the container to /app
WORKDIR /app

# Add the current directory contents into the container at /app
ADD . /app

RUN apt-get update

RUN apt-get install -y ffmpeg

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Run the command to start uWSGI
CMD ["sh", "-c", "uvicorn main:app --host $HOST --port $PORT"]
