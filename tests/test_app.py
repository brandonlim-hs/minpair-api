from app import app
import json
import pytest


def test_index():
    app.testing = True
    response = app.test_client().get("/")
    assert b"minpair API" in response.data


def test_vowel_minpair():
    app.testing = True
    response = app.test_client().get("/vowel?vowels=AE&vowels=EH")
    assert {
        "AE": "last",
        "EH": "less"
    } in json.loads(response.data.decode("utf-8"))["minimal_pairs"]
