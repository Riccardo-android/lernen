from flask import Flask, Response
import requests
from prometheus_client import Gauge, generate_latest

app = Flask(__name__)

warning_level = Gauge('dwd_warning_level', 'DWD Warnstufe', ['region'])




@app.route("/metrics")
def metrics():
    url = "https://opendata.dwd.de/weather/alerts/json/capWarnings.json"
    level = 0
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200 and response.headers.get('Content-Type', '').startswith('application/json'):
            data = response.json()
            warnungen = data.get('warnings', {}).get('110000000', [])
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

    warning_level.labels(region="110000000").set(level)
    return Response(generate_latest(), mimetype="text/plain")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9110)
