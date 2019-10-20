from urllib.parse import urlencode
import json
import pytest


def test_index(client):
    response = client.get("/")
    assert b"minpair API" in response.data


@pytest.mark.parametrize(
    ("vowels", "pos", "expected_minimal_pairs"),
    (
        (["AE", "EH"], [], [{"AE": "bad", "EH": "bed"},
                            {"AE": "last", "EH": "less"}]),
        (["AE", "EH"], ["ADJ"], [{"AE": "last", "EH": "less"}]),
        (["AE", "EH", "IH"], [], [{"AE": "bad", "EH": "bed", "IH": "bid"}]),
    )
)
def test_vowel_minpair(client, vowels, pos, expected_minimal_pairs):
    query = urlencode({
        "vowels": vowels,
        "pos": pos,
    }, True)
    response = client.get("/vowel?" + query)
    minimal_pairs = json.loads(response.data.decode("utf-8"))["minimal_pairs"]
    assert all(
        minimal_pair in minimal_pairs
        for minimal_pair in expected_minimal_pairs
    )


@pytest.mark.parametrize(
    ("vowels", "pos", "expected_message"),
    (
        ([], [], "At least a pair of unique vowels required."),
        (["AE", "B"], [], "Only vowels are accepted."),
    )
)
def test_vowel_minpair_validate_input(client, vowels, pos, expected_message):
    query = urlencode({
        "vowels": vowels,
        "pos": pos,
    }, True)
    response = client.get("/vowel?" + query)
    errors = json.loads(response.data.decode("utf-8"))["errors"]
    assert {"message": expected_message} in errors
