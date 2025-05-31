## READMETEST.md
    # Software-Development/Vernisage-Project

    > Dieses Projekt sammelt Wetterdaten von einer Wetterdatenquelle, 
    > expotiert diese als Prometheus Metriken und Sie in Grafana 
    > visualisieren als Dashboard dar.

## Features 
    - Wetterdaten von verschiedenen Wetterstationen ab 1990
    - Historische Temperaturverläufe 
    - Automatische Speicherung in SQL-Datenbank

## Website
    - https://github.com/Friedfisch19/Software-Development.git

## Anforderungen
    - Python 3.12 oder höher
    - Docker (für die Containerisierung)
    - Git (für die Versionskontrolle)

## GIT
    - Um das Projekt zu klonen, verwenden Sie den folgenden Befehl:
    ```bash
    git clone git@github.com:Friedfisch19/Software-Development.git
    ``` 

## Docker
    - Stellen Sie sicher, dass Docker installiert ist.
    - Navigieren Sie zum Verzeichnis `src/Docker`.
    - Führen Sie den folgenden Befehl aus, um das Docker-Image zu erstellen und den Container zu starten:
    ```bash
    docker compose up --build
    ```
    - Dies startet die Anwendung und die Datenbank im Hintergrund.
    - Der Zusatz --build ist nur einmalig nötig, um die Images zu erstellen

## Datenbank
    - Die Anwendung verwendet eine SQL-Datenbank, die automatisch im Docker-Container erstellt wird.
    - Die Datenbank ist für die Speicherung der Wetterdaten konfiguriert.

## Nutzung
    - Nach dem Starten des Docker-Containers können Sie die Anwendung über Ihren Webbrowser aufrufen.
    - Die Anwendung bietet eine Benutzeroberfläche zur Analyse und Visualisierung der Wetterdaten.

## Projektstruktur
    - ...


    







