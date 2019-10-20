import json


def test_index(client):
    response = client.get("/")
    assert b"minpair API" in response.data


def test_vowel_minpair(client):
    response = client.get("/vowel?vowels=AE&vowels=EH")
    assert {
        "AE": "last",
        "EH": "less"
    } in json.loads(response.data.decode("utf-8"))["minimal_pairs"]
