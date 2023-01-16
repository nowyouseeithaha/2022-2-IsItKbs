#Pytest
import pytest
from isitkbs import is_kbs

@pytest.mark.parametrize("mashings, result1", [
    ("ldkajs", 1),
    ("acljnsd", 1),
    ("aaaaaaaa", 1),
    (".2dasd", 1),
    ("klhebdf", 1),
    ("xlapzlx", 1),
    ("hellohjsbahjc", 1),
    ("mzxkzxc", 1),
    ("peqweqwe", 1),
])

def test_mashings(mashings, result1):
    assert is_kbs(input_data = mashings) == result1


@pytest.mark.parametrize("nonmashings, result2", [
    ("home", 0),
    ("about", 0),
    ("page", 0),
    ("search", 0),
    ("view", 0),
    ("other", 0),
    ("information", 0),
    ("time", 0),
    ("business", 0),
    ("world", 0),
])

def test_nonmashings(nonmashings, result2):
    assert is_kbs(input_data = nonmashings) == result2

