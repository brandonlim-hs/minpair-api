from app import app
import pytest


@pytest.fixture
def client():
    """A test client for the app."""
    app.testing = True
    return app.test_client()
