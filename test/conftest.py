import json

import pytest
import pandas as pd
from src.transform import transform_request

@pytest.fixture
def load_sample_data(sample_json):

    df = transform_request(sample_json)
    return df



@pytest.fixture
def sample_json():
    with open("test/data/test_response.json") as user_file:
        file_contents = user_file.read()

    parsed_json = json.loads(file_contents)
    return parsed_json
