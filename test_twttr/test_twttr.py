from twttr import shorten

def test_lowercase():
    assert shorten("this is a test") == "ths s  tst"

def test_uppercase():
    assert shorten("THIS IS A TEST") == "THS S  TST"

def test_mixedcase():
    assert shorten("This Is A Test") == "Ths s  Tst"
