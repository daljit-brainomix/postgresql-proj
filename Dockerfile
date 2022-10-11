# pull base image
FROM python:3.8.10

# Set environment vars
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code

# Copy project
COPY . /code/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt