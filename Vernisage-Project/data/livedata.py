from flask import Flask, Response
from prometheus_client import CollectorRegistry, Gauge, generate_latest
import openmeteo_requests
import requests_cache
from retry_requests import retry
from datetime import datetime
import sqldatadef
import mysql.connector
# Initialisierung der Flask-Anwendung
app = Flask(__name__)

sqldatadef.database("cities_current")

# Konfiguration des Open-Meteo API Clients mit Caching und Retry-Mechanismus
# Cache wird für 1 Stunde (3600 Sekunden) gespeichert
# Retry-Mechanismus versucht fehlgeschlagene Anfragen bis zu 5 mal
cache_session = requests_cache.CachedSession('.cache', expire_after=3600)
retry_session = retry(cache_session, retries=5, backoff_factor=0.2)
openmeteo = openmeteo_requests.Client(session=retry_session)

# Liste der Standorte mit ihren geografischen Koordinaten
# Jeder Standort wird durch Name, Breitengrad (lat) und Längengrad (lon) definiert
locations = [
    {"name": "Jeju", "lat": 33.4996, "lon": 126.5312},
    {"name": "Goiania", "lat": -16.6786, "lon": -49.2539},
    {"name": "Troll", "lat": -72.011, "lon": 2.535},
    {"name": "Muenchen", "lat": 48.1371, "lon": 11.5754},
    {"name": "Brocken", "lat": 51.7996, "lon": 10.6190},
    {"name": "Itzehoe", "lat": 53.9210, "lon": 9.5176}, #zusätzliche Stadt kann hinzugefügt werden
]
#sqlite3 db setup
#cnx = mysql.connector.connect(host="db", port=3306, user="root", passwd="Pr!m4bAl13rina")
#cursor = cnx.cursor()


createtable = """CREATE TABLE IF NOT EXISTS livedata (
                                                        `id` int NOT NULL AUTO_INCREMENT,
                                                        `city` varchar(255) NOT NULL ,
                                                         `date` varchar(255) NOT NULL,
                                                         `time` varchar(255) NOT NULL,
                                                          `temperature` float NOT NULL,
                                                          `humidity` float NOT NULL, 
                                                          `rain` float NOT NULL,
                                                           PRIMARY KEY (`id`, `City`,`temperature`,`humidity`, `rain`)
                                                            ) ENGINE=InnoDB
                                                            """
with sqldatadef.cnx.cursor() as cursor:
    cursor.execute(createtable)
    sqldatadef.cnx.commit()




def save_cities_current(city, temperature, humidity, rain):
    """
    Speichert die Wetterdaten in der SQLite-Datenbank.
    """
    now = datetime.now()
    date_str = now.strftime("%d-%m-%Y")
    time_str = now.strftime("%H:%M:%S")
    zsm = (city, date_str, time_str, temperature, humidity, rain)
    insert = """INSERT INTO livedata (city, date, time, temperature, humidity, rain)
            VALUES (%s, %s, %s, %s, %s, %s)"""
    with sqldatadef.cnx.cursor() as cursor:
        cursor.execute(insert, zsm)
        sqldatadef.cnx.commit()

@app.route("/metrics")
def metrics():
    # Erstellung eines neuen Prometheus Registry-Objekts für die Metriken
    registry = CollectorRegistry()

    # Definition der Prometheus-Metriken (Gauges) für verschiedene Wetterdaten
    # Jede Metrik wird mit einem Namen, einer Beschreibung und einem Label für die Stadt versehen
    g_temp = Gauge("openmeteo_temperature_celsius", "Temperatur in °C", ["city"], registry=registry)
    g_humidity = Gauge("openmeteo_humidity_percent", "Luftfeuchtigkeit in %", ["city"], registry=registry)
    g_rain = Gauge("openmeteo_rain_mm", "Regen in mm", ["city"], registry=registry)

    # Iteration durch alle definierten Standorte
    for loc in locations:
        # Parameter für die Open-Meteo API-Anfrage
        params = {
            "latitude": loc["lat"],
            "longitude": loc["lon"],
            "current": ["temperature_2m", "relative_humidity_2m", "rain"],
            "timezone": "auto"
        }
        try:
            # API-Anfrage an
            responses = openmeteo.weather_api("https://api.open-meteo.com/v1/forecast", params=params)
            current = responses[0].Current()
            #eine nachkommastelle für die Temperatur und rain in mm
            temperature = float(f"{current.Variables(0).Value():.1f}")
            rain = float(f"{current.Variables(2).Value():.1f}")
            humidity = float(f"{current.Variables(1).Value():.1f}")
            g_temp.labels(city=loc["name"]).set(temperature)
            g_humidity.labels(city=loc["name"]).set(humidity)
            g_rain.labels(city=loc["name"]).set(rain)

            save_cities_current(loc["name"], temperature, humidity, rain)

        except Exception as e:
            print(f"Fehler bei {loc['name']}: {e}")

    return Response(generate_latest(registry), mimetype="text/plain")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)

