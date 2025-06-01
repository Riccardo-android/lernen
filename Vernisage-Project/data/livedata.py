import requests


url = "https://open-meteo.com/en/docs/historical-weather-api"

response = requests.get(url)
file = response.text
print(file)