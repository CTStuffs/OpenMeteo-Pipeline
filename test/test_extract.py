import json

import requests

import pytest
from unittest.mock import patch, mock_open, MagicMock, Mock
from src.extract import get_request

@patch("src.extract.requests.get")
def test_successful_api_request(mock_get):
    fake_response = Mock()
    fake_response.json.return_value = {
        "test": 22,
        "testval2": "Sunny"
    }
    fake_response.raise_for_status.return_value = None

    mock_get.return_value = fake_response

    result = get_request()

    assert result == {
        "test": 22,
        "testval2": "Sunny"
    }

    mock_get.assert_called_once()


@patch("src.extract.requests.get")
def test_http_error_handling(mock_get):
    fake_response = Mock()
    fake_response.json.return_value = {
        "error": "error message"
    }
    fake_response.raise_for_status.side_effect = (
        Exception("500 Server Error")
    )

    mock_get.return_value = fake_response
    with pytest.raises(Exception):
        get_request()

@patch("src.extract.requests.get")
def test_file_write_success(mock_get):
    fake_response = Mock()
    fake_response.json.return_value = "test"
    
    fake_response.raise_for_status.return_value = None
    mock_get.return_value = fake_response
    mocked_file = mock_open()

    
    with patch("builtins.open", mocked_file):
        get_request()
        mocked_file.assert_called_once_with("./data/raw_data.json", "a")
        handle = mocked_file()
        handle.write.assert_called_once_with(json.dumps(fake_response.json.return_value, indent=2))

def test_file_write_error_handling():
    """Verify IOError is caught and logged when file write fails."""
    pass


def test_return_value():
    """Verify the function returns the parsed JSON response."""
    pass
