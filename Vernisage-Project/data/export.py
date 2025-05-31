from flask import Flask, Response
import requests
from prometheus_client import Gauge, generate_latest

app = Flask(__name__)

# Prometheus Gauge-Metrik für DWD-Warnstufen
# Warnstufen: 0 (keine Warnung), 1 (moderat), 2 (schwer), 3 (extrem)
warning_level = Gauge('dwd_warning_level', 'DWD Warnstufe', ['region'])

@app.route("/metrics")
def metrics():
    # DWD OpenData API-Endpunkt für Wetterwarnungen
    url = "https://opendata.dwd.de/weather/alerts/json/capWarnings.json"
    level = 0
    
    try:
        # Abrufen der Warnungen mit Timeout von 10 Sekunden
        response = requests.get(url, timeout=10)
        
        # Überprüfen ob die Antwort gültig ist und JSON enthält
        if response.status_code == 200 and response.headers.get('Content-Type', '').startswith('application/json'):
            data = response.json()
            # Extrahieren der Warnungen für Region 110000000 (Berlin)
            warnungen = data.get('warnings', {}).get('110000000', [])
            
            # Ermitteln der höchsten Warnstufe aus allen aktiven Warnungen
            for warnung in warnungen:
                severity = warnung.get('severity', '')
                if severity == "Extreme":
                    level = max(level, 3)
                elif severity == "Severe":
                    level = max(level, 2)
                elif severity == "Moderate":
                    level = max(level, 1)
        else:
            print(f"Fehlerhafte Antwort vom DWD-Server: {response.status_code}, Inhalt: {response.text[:200]}")
    except Exception as e:
        print("Fehler beim Abrufen oder Verarbeiten der DWD-Daten:", e)

    # Aktualisieren der Prometheus-Metrik mit der höchsten Warnstufe
    warning_level.labels(region="110000000").set(level)
    # Generieren und Zurückgeben der Prometheus-Metriken im korrekten Format
    return Response(generate_latest(), mimetype="text/plain")

if __name__ == "__main__":
    # Server-Start auf allen Interfaces (0.0.0.0) und Port 9110
    app.run(host="0.0.0.0", port=9110)