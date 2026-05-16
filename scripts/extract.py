import requests
import json
locations = [
    {"city": "Melbourne", "lat": -37.81, "lon": 144.96},
    {"city": "Sydney", "lat": -33.86, "lon": 151.20}
]
responses = requests.get(f'https://api.open-meteo.com/v1/forecast?latitude={locations[0]["lat"]}&longitude={locations[0]["lon"]}&current_weather=true')

with open("./data/raw_data.json", "a") as f:
  f.write(json.dumps(responses.json(), indent=2))

