from app import app
import pytest


def test_index():
    app.testing = True
    response = app.test_client().get("/")
    assert b"index" in response.data
