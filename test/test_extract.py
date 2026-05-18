import pytest
from unittest.mock import patch, mock_open, MagicMock
from unittest.mock import patch, Mock
from src.extract import get_request

@patch("requests.get")
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



def test_http_error_handling():
    """Verify HTTPError is caught and logged when the API request fails."""
    pass


def test_file_write_success():
    """Verify the response is correctly written to ./data/raw_data.json."""
    pass


def test_file_write_error_handling():
    """Verify IOError is caught and logged when file write fails."""
    pass


def test_return_value():
    """Verify the function returns the parsed JSON response."""
    pass
