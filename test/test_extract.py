"""
Test skeletons for src/extract.py

Each test is a pytest function with a descriptive docstring outlining the
setup, mocks, and assertions to implement. Bodies raise NotImplementedError so
you can fill in the test code yourself.
"""

import pytest


def test_successful_api_call_returns_json_and_writes_file(monkeypatch, tmp_path, caplog):
    """Mock `requests.get` to return a known JSON payload. Use `tmp_path` or
    patch `open` to capture file writes. Assert:
    - `get_request()` returns the expected dict
    - `requests.get` was called with the Melbourne coordinates URL
    - the file was opened in append mode and written with the response JSON
    """
    raise NotImplementedError("Implement test: successful API call returns JSON and writes file")


def test_request_url_correctness(monkeypatch):
    """Mock `requests.get` and capture the requested URL. Assert that the
    URL contains the latitude/longitude for the first location and
    `current_weather=true`.
    """
    raise NotImplementedError("Implement test: request URL correctness")


def test_http_error_from_requests_is_handled_and_logged(monkeypatch, caplog):
    """Have `requests.get` raise `requests.exceptions.HTTPError`. Assert an
    error log entry is emitted and the function behaves as documented
    (e.g., returns None or raises). Document expected behavior in the test.
    """
    raise NotImplementedError("Implement test: HTTPError handling and logging")


def test_connection_error_handling(monkeypatch, caplog):
    """Simulate `requests.exceptions.ConnectionError` from `requests.get`.
    Verify appropriate logging and behavior consistent with HTTPError case.
    """
    raise NotImplementedError("Implement test: ConnectionError handling")


def test_io_error_during_file_write_is_handled_and_logged(monkeypatch, caplog):
    """Mock `requests.get` to succeed but patch `open` to raise `IOError`.
    Assert an error log entry and that the function's return behavior is
    documented and asserted.
    """
    raise NotImplementedError("Implement test: IOError during file write handling")


def test_file_append_semantics(monkeypatch, tmp_path):
    """On two consecutive successful calls (mocking `requests.get`), verify
    that file contents accumulate (append mode) rather than being overwritten.
    Use `tmp_path` to create an isolated file path.
    """
    raise NotImplementedError("Implement test: file append semantics")
