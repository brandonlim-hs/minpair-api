from app import app
import pytest


def test_index():
    app.testing = True
    response = app.test_client().get("/")
    assert b"minpair API" in response.data
