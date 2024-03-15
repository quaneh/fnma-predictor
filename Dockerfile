# Use a base image
FROM python:3.10

# Installing packages
RUN apt-get update
RUN pip install --no-cache-dir pipenv

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the pip files to the container
COPY Pipfile ./

# Install the required packages using pip
RUN pipenv install

# Copy the application files to the container
COPY . .

# Specify the command to run the application using Gunicorn
EXPOSE 80
CMD ["pipenv", "run", "gunicorn", "--workers", "4", "--bind", "0.0.0.0:80", "app:app"]