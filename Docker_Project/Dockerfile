# Use the official Python image from the Docker Hub
FROM python:3.11

# Set the working directory
WORKDIR /code

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Install gunicorn
RUN pip install gunicorn

# Copy the project files
COPY . .


# Run Django server
CMD ["gunicorn", "Docker_Project.wsgi:application", "--bind", "0.0.0.0:8000"]
