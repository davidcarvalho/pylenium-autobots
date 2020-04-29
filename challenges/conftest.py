import pytest


@pytest.fixture
def copart(py):
    py.visit('https://www.copart.com/')
    return py
