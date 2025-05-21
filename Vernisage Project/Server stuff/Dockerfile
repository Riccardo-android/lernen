FROM alpine:3.13

# Wenn ein anderes Image auf diesem basiert, wird coreutils dann installiert
RUN apk add --no-cache coreutils

FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY export.py .

EXPOSE 9110

CMD ["python", "export.py"]

# Start with a lightweight base image
#FROM alpine:latest

# Install SQLite
#RUN apk update && apk add sqlite

# Set the default working directory
#WORKDIR /db

# Set the default command to open SQLite
#CMD ["sqlite3"]

