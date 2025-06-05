# Basis-Image mit Python 3.12
FROM python:3.12

# Setze das Arbeitsverzeichnis im Container
WORKDIR /app

# Kopiere die Requirements-Datei und installiere die Abhängigkeiten
# Dies wird als separater Schritt ausgeführt, um den Docker-Cache zu nutzen
COPY data/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Kopieren uns die Python scripts auf den Container die in diesem verwendet werden
COPY data/sqldatadef.py .
COPY data/sqldata.py .
COPY data/histflive.py .
COPY data/histflivefunc.py .

# Definiere den Port, der vom Container freigegeben wird
EXPOSE 3307

# Starte die Python-Anwendung
CMD ["python", "sqldata.py"]
