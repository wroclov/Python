# Import pytest library
import pytest


# Creating the common function for input
@pytest.fixture
def string_match():
    string = "Geeks For Geeks"
    return string.strip()


# Creating first test case
def test_remove_G(string_match):
    assert string_match.replace('G', '') == "eeks For eeks"


# Creating second test case
def test_remove_e(string_match):
    assert string_match.replace('e', '') == "Gks For Gks"


# Creating third test case
def test_remove_o(string_match):
    assert string_match.replace('o', '') == "Geeks Fr Geeks"
