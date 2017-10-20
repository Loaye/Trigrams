import pytest

def test_open_source():
    from trigrams import open_source
    text = open_source('./sample.txt')
    assert type(text) is str
    assert len(text) > 1

def test_make_trigrams():
    from trigrams import make_trigrams
    trigrams = make_trigrams("1 2 3 4 5 6 7 8 9")
    assert type(trigrams) == dict
    for key, value in trigrams.items():
        assert type(value) is list


def test_generate_text():
    from trigrams import generate_text
    wordlist = generate_text({'a b' : ['b', 'c'], 'foo bear' : ['bar']}, 10)
    assert len(wordlist) == 10
