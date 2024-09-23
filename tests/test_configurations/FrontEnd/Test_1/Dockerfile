# Python Aplication Dockerfile
# Fask Aplication Dockerfile

# Avoid using latest tag in production
FROM python:latest

WORKDIR /app

COPY . /app
# Install the application dependencies
RUN pip install --no-cache-dir -r requirements.txt
# Run the application using Gunicorn
CMD ["gunicorn", "-w", "", "-b", ":80", ":"]

EXPOSE 80
