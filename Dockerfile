## Use the official Python image from DockerHub
#FROM python:3.10-slim
#
## Set environment variables to ensure Python output is not buffered and not compiled
#ENV PYTHONDONTWRITEBYTECODE=1
#ENV PYTHONUNBUFFERED=1
#
## Install system dependencies
#RUN apt-get update && apt-get install -y \
#    libpq-dev gcc && \
#    apt-get clean
#
## Set the working directory inside the container
#WORKDIR /app
#
## Copy requirements.txt to the container
#COPY requirements.txt /app/
#
## Install dependencies
#RUN pip install --upgrade pip && \
#    pip install -r requirements.txt
#
## Copy the rest of the Django project to the container
#COPY project /app/
#
## Expose the port on which Django will run (default: 8000)
#EXPOSE 8000
#
## Run the Django application
#CMD ["gunicorn", "--bind", "0.0.0.0:8000", "myproject.wsgi:application"]
