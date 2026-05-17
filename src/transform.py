
import pandas as pd
def transform_request(dict):
    # df = pd.read_json(json["current_weather"])
    df = pd.DataFrame(dict["current_weather"], index=[0])

    # print(df)

    # then clean the data

    df["time"] = pd.to_datetime(df['time'], format='ISO8601')
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
    print(df)

    # then rename the columns into something more meaningful

    # then set the columns to the appropriate data type

    return df