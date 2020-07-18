# Use latest Python runtime as a parent image
FROM python:3.6.5-alpine3.7
FROM tensorflow/tensorflow:2.1.0-py3

# Meta-data

      
ENV HOME=/app
# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# pip install
RUN pip --no-cache-dir install -r requirements.txt

# Make port available to the world outside this container
EXPOSE 8080

# Create mountpoint
VOLUME /app/data

# ENTRYPOINT allows us to specify the default executible
#ENTRYPOINT ["python"]

# CMD sets default arguments to executable which may be overwritten when using docker run
CMD ["gunicorn", "-c", "gunicorn_config.py", "server:app"]