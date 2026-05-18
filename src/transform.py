
import pandas as pd
import logging

logger = logging.getLogger(__name__)
def transform_request(dict):
    df = pd.DataFrame(dict["current_weather"], index=[0])
    logger.info("Transforming data...")

    df = df.drop_duplicates()
    df = df.dropna()

    df["time"] = pd.to_datetime(df['time'], format=dict['current_weather_units']['time'])
    df["interval"] = df["interval"].astype(int)
    df["temperature"] = df["temperature"].astype(float)
    df["windspeed"] = df["windspeed"].astype(int)
    df["winddirection"] = df["winddirection"].astype(float)
    df["weathercode"] = df["weathercode"].astype(int)
    df["is_day"] = df["weathercode"].astype(bool)

    df.rename(columns = {
        "temperature": "temperature_celsius",
        "windspeed": "windspeed_km_per_hr",
        "winddirection": "winddirection_degrees",
        "interval": "interval_seconds",

    }, inplace=True)
    logger.info("Transform success!")
    return df