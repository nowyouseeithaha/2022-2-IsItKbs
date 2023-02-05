#Pytest
import pytest
from isitkbs import isitkbs

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

def test_wordm(mashings, result1):
    w = isitkbs()
    assert w.wordkbs(input_data = mashings) == result1

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

def test_wordn(nonmashings, result2):
    wn = isitkbs()
    assert wn.wordkbs(input_data = nonmashings) == result2

@pytest.mark.parametrize("phrases, result3", [
    ("This is a asdjhasijd", ["asdjhasijd"]),
    ("a", []),
    ("b", []),
    ("The world is a beautiful place", []),
    ("Be careful ieieieie", ["ieieieie"]),
    ("It's time to dudududuel", ["dudududuel"]),
    ("This is just a akdshjsaj message aaaaaa", ["akdshjsaj", "aaaaaa"]),
    ("I love batataaskdhjaksj", ["batataaskdhjaksj"])
])

def test_phrases(phrases, result3):
    ph = isitkbs()
    assert ph.sentkbs(input_data = phrases) == result3