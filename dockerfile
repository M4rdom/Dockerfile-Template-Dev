# Python Aplication Dockerfile
# Fask Aplication Dockerfile

FROM python:3.13.0-alpine3.20

# Keeps Python from buffering stdout and stderr to avoid situations where
# the application crashes without emitting any logs due to buffering.
ENV PYTHONUNBUFFERED=1

# Create a non-privileged user that the app will run under.
# See https://docs.docker.com/go/dockerfile-user-best-practices/
ARG UID=10001
RUN adduser \
    --disabled-password \
    --gecos "" \
    --home "/nonexistent" \
    --shell "/sbin/nologin" \
    --no-create-home \
    --uid "${UID}" \
    appuser


WORKDIR /app

COPY . /app
# Install the application dependencies
RUN --mount=type=cache,target=/root/.cache/pip \
    python -m pip install --no-cache-dir -r requirements.txt


# Install Gunicorn This is not recommended for production, requirements.txt should be used instead

RUN pip install --no-cache-dir -r gunicorn==23.0.0

USER appuser

# Run the application using Gunicorn
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:80", "app:app"]

# Make port 5000 available to the world outside this container
EXPOSE 5000
