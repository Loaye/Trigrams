import pytest

def test_open_file():
    from trigrams import open_source
    assert len(open_source('./sample.txt'))    
