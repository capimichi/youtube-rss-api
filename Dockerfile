# Use an official Python runtime as a parent image
FROM python:3.11

# Define environment variables
ENV HOST 0.0.0.0
ENV PORT 80
ENV BASE_URL http://{HOST}:{PORT}

# Set the working directory in the container to /app
WORKDIR /app

# Add the current directory contents into the container at /app
ADD requirements.txt /app/requirements.txt

RUN apt-get update

RUN apt-get install -y ffmpeg

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Install curl and Node.js
RUN apt-get install -y curl
# RUN apt install nodejs npm -y

# Install yarn
# RUN npm install -g yarn

# Change to docusaurus directory, install dependencies and build
# RUN cd docusaurus && yarn install && yarn build

# Make port 80 available to the world outside this container
EXPOSE 80

# Run the command to start uWSGI
CMD ["sh", "-c", "uvicorn main:app --host $HOST --port $PORT"]
