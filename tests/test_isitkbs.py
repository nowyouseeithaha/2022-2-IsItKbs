#Pytest
import pytest
import pandas as pd
from isitkbs import isitkbs

 #Testes com Randomforest
@pytest.fixture
def rf_object():
    return isitkbs("randomforest")

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

def test_word_mashing_randomforest(rf_object, mashings, result1):
    assert rf_object.wordkbs(input_data = mashings) == result1

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
    ("glass", 0),
    ("my", 0),
    ("Incomprehensibilities", 0),
    ("as", 0),
    ("pizza", 0),
    ("pneumonoultramicroscopicsilicovolcanoconiosis", 0),
])

def test_word_nonmashing_randomforest(rf_object,nonmashings, result2):
    assert rf_object.wordkbs(input_data = nonmashings) == result2

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

def test_phrases_randomforest(rf_object, phrases, result3):
    assert rf_object.sentkbs(input_data = phrases) == result3

 #Testes com NaiveBayes
@pytest.fixture
def nb_object():
    return isitkbs("naivebayes")

@pytest.mark.parametrize("mashings, result1", [
    ("ldkajs", 1),
    ("acljnsd", 1),
    ("aaaaaaaa", 1),
    (".2dasd", 1),
    ("klhebdf", 1),
    ("xlapzlx", 1),
    ("jsbahjc", 1),
    ("mzxkzxc", 1),
    ("peqweqwe", 1),
])

def test_word_mashing_naivebayes(nb_object,mashings, result1):
    assert nb_object.wordkbs(input_data = mashings) == result1

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
    ("glass", 0),
    ("my", 0),
    ("Incomprehensibilities", 0),
    ("as", 0),
    ("actually", 0),
    ("pneumonoultramicroscopicsilicovolcanoconiosis", 0),
])

def test_word_nonmashing_naivebayes(nb_object, nonmashings, result2):
    assert nb_object.wordkbs(input_data = nonmashings) == result2

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

def test_phrases_naivebayes(nb_object, phrases, result3):
    assert nb_object.sentkbs(input_data = phrases) == result3

def test_wordkbs_input_type(nb_object):
    with pytest.raises(TypeError): 
        nb_object.wordkbs(123)

def test_sentkbs_input_type(nb_object):
    assert nb_object.sentkbs(123) == []

 # Usamos essa parte so no naivebayes porque independe do modelo e o nb e mais rapido
def test_list_input_sent_kbs(nb_object):
    assert nb_object.sentkbs(["Hello"]) == []

def test_phrases_list_sent_kbs(nb_object):
    assert nb_object.sentkbs(["This is a normal phrase"]) == []

def test_num_list_sent_kbs(nb_object):
    assert nb_object.sentkbs([53, 'asdas', 'Hello']) == ['asdas']

def test_freqkbs(nb_object):
    assert nb_object.freqkbs("sdkaodk", graph=0) == {'a': 1, 'd': 2, 'k': 2, 'o': 1, 's': 1}
    
def test_freqkbs_graph(nb_object):
    assert nb_object.freqkbs("sdkaodk", graph=1) == {'a': 1, 'd': 2, 'k': 2, 'o': 1, 's': 1}

def test_replacekbs_string(nb_object):
    assert nb_object.replacekbs(input_data = "This is a sdksj") == "This is a"

def test_replacekbs_null_dataframe(nb_object):
    df = pd.DataFrame(["This", "is", "a", "sdasdafg", "dataframe"])
    assert nb_object.replacekbs(input_data = df).to_dict() == {0: {0: 'This', 1: 'is', 2: 'a', 3: 'dataframe'}}

def test_replacekbs_str_dataframe_justword(nb_object):
    df = pd.DataFrame(["This", "is", "a", "normal sdasdafg", "dataframe"])
    assert nb_object.replacekbs(input_data = df, value = "REMOVIDO", just_word = True).to_dict() == {0: {0: 'This', 1: 'is', 2: 'a', 3: 'normal REMOVIDO', 4: 'dataframe'}}

def test_replacekbs_str_dataframe(nb_object):
    df = pd.DataFrame(["This", "is", "a", "normal sdasdafg", "dataframe"])
    assert nb_object.replacekbs(input_data = df, value = "REMOVIDO").to_dict() == {0: {0: 'This', 1: 'is', 2: 'a', 3: 'REMOVIDO', 4: 'dataframe'}}

def test_replacekbs_string(nb_object):
    assert nb_object.replacekbs(input_data = ["This is a sdksj"], just_word=True) == ["This is a"]