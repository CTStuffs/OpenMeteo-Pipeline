import json

import requests
import pytest
from unittest.mock import patch, mock_open, MagicMock, Mock
from src.extract import get_request


def test_successful_api_request():
    fake_response = Mock()
    fake_response.json.return_value = {
        "test": 22,
        "testval2": "Sunny"
    }
    fake_response.raise_for_status.return_value = None

    with patch("src.extract.requests.get", return_value=fake_response) as mock_get:
        result = get_request()

    mock_get.assert_called_once()
    assert result == {
        "test": 22,
        "testval2": "Sunny"
    }


def test_http_error_handling():
    fake_response = MagicMock()
    fake_response.json.return_value = {
        "error": "error message"
    }
    fake_response.raise_for_status.side_effect = (
        requests.exceptions.HTTPError("500 Server Error")
    )

    with patch("src.extract.requests.get", return_value=fake_response):
        with pytest.raises(requests.exceptions.HTTPError):
            get_request()


def test_file_write_success():
    fake_response = MagicMock()
    fake_response.json.return_value = "test"
    fake_response.raise_for_status.return_value = None
    mocked_file = mock_open()

    with patch("src.extract.requests.get", return_value=fake_response), \
         patch("builtins.open", mocked_file):
        get_request()

    mocked_file.assert_called_once_with("./data/raw_data.json", "a")
    handle = mocked_file()
    handle.write.assert_called_once_with(json.dumps(fake_response.json.return_value, indent=2))


def test_file_write_error_handling():
    fake_response = MagicMock()
    fake_response.json.return_value = "test"
    fake_response.raise_for_status.return_value = None
    mocked_file = mock_open()
    mocked_file.side_effect = IOError("File write error")

    with patch("src.extract.requests.get", return_value=fake_response), \
         patch("builtins.open", mocked_file):
        get_request()


def test_return_value():
    fake_response = MagicMock()
    fake_response.json.return_value = {
        "test": 22,
        "testval2": "Sunny"
    }
    fake_response.raise_for_status.return_value = None

    with patch("src.extract.requests.get", return_value=fake_response):
        result = get_request()

    assert result == {
        "test": 22,
        "testval2": "Sunny"
    }
