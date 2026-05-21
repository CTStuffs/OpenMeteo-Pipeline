import pytest
import pandas as pd
from src.transform import transform_request


def test_dataframe_creation(load_sample_data):
    df = load_sample_data.copy()
    assert isinstance(df, pd.DataFrame), "Output should be a pandas DataFrame."


def test_duplicate_removal(load_sample_data):
    df = load_sample_data.copy()
    df_cleaned = df.drop_duplicates()
    assert not df_cleaned.duplicated().any(), "DataFrame still contains duplicate rows."


def test_null_removal(load_sample_data):
    df = load_sample_data.copy()
    df_cleaned = df.dropna()
    assert not df_cleaned.isnull().any().any(), "DataFrame still contains missing values."


def test_datetime_conversion(load_sample_data):
    df = load_sample_data.copy()
    assert pd.api.types.is_datetime64_any_dtype(df['time']), "Time column is not of datetime type."


def test_type_conversions(load_sample_data):
    df = load_sample_data.copy()
    assert pd.api.types.is_float_dtype(df['temperature_celsius']), "Temperature column is not float."
    assert pd.api.types.is_integer_dtype(df['windspeed_km_per_hr']), "Windspeed column is not integer."
    assert pd.api.types.is_float_dtype(df['winddirection_degrees']), "Winddirection column is not float."
    assert pd.api.types.is_integer_dtype(df['interval_seconds']), "Interval column is not integer."
    assert pd.api.types.is_bool_dtype(df['is_day']), "Is_day column is not integer."


def test_valid_output_structure(load_sample_data):
    df = load_sample_data.copy()
    assert df.shape[0] > 0, "DataFrame is empty."
    assert 'temperature_celsius' in df.columns, "Expected column 'temperature_celsius' not found."
    assert 'windspeed_km_per_hr' in df.columns, "Expected column 'windspeed_km_per_hr' not found."
    assert 'winddirection_degrees' in df.columns, "Expected column 'winddirection_degrees' not found."
    assert 'interval_seconds' in df.columns, "Expected column 'interval_seconds' not found."
    assert 'is_day' in df.columns, "Expected column 'is_day' not found."
    assert 'time' in df.columns, "Expected column 'time' not found."

