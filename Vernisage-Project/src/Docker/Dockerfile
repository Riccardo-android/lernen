FROM alpine:3.13 as tools

# Wenn ein anderes Image auf diesem basiert, wird coreutils dann installiert
RUN apk add --no-cache coreutils

FROM python:3.12-slim

WORKDIR /app

COPY ../../requirements.txt .
#COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

#COPY ../../data/export.py .
COPY data/livedata.py .
COPY data/sqldatadef.py .

EXPOSE 9110

CMD ["python", "livedata.py"]


#FROM node:latest
#WORKDIR /app
#COPY package.json ./
#RUN npm install
#COPY . .
#EXPOSE 3001
#CMD [ "node", "index.js"]

# Start with a lightweight base image
#FROM alpine:latest

# Install SQLite
#RUN apk update && apk add sqlite

# Set the default working directory
#WORKDIR /db

# Set the default command to open SQLite
#CMD ["sqlite3"]

