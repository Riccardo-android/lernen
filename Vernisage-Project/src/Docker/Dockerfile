FROM alpine:3.13 as tools

# Wenn ein anderes Image auf diesem basiert, wird coreutils dann installiert
RUN apk add --no-cache coreutils

FROM python:3.12-slim

WORKDIR /app

COPY ../../requirements.txt .
#COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt      #installiert die notwendigen Packages sofern sie via pip installierbar sind

#COPY ../../data/export.py .
COPY data/livedata.py .
COPY data/sqldatadef.py .

EXPOSE 9110

CMD ["python", "livedata.py"]
