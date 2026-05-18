import requests
import json
import logging

logger = logging.getLogger(__name__)

def get_request():
  locations = [
      {"city": "Melbourne", "lat": -37.81, "lon": 144.96},
      {"city": "Sydney", "lat": -33.86, "lon": 151.20}
  ]


  logger.info("Retrieving data from OpenMeteo...")
  try:
    responses = requests.get(f'https://api.open-meteo.com/v1/forecast?latitude={locations[0]["lat"]}&longitude={locations[0]["lon"]}&current_weather=true')
  except requests.exceptions.HTTPError as errh:
    logger.error("HTTP Error:", errh)
    
  logger.info("Retrieval success!")

  logger.info("Writing data to file...")

  try:
    with open("./data/raw_data.json", "a") as f:
      f.write(json.dumps(responses.json(), indent=2))
  except IOError as err:
    logger.error("IO Error:", err)
  logger.info("Write success!")

  return responses.json()

