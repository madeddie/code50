from twttr import shorten

def test_lowercase():
    assert shorten("this is a test") == "ths s  tst"

def test_uppercase():
    assert shorten("THIS IS A TEST") == "THS S  TST"

def test_mixedcase():
    assert shorten("This Is A Test") == "Ths s  Tst"

def test_noreplace():
    assert shorten("Nthng hppns") == "Nthng hppns"

def test_numbers():
    assert shorten("Testing 123") == "Tstng 123"

def test_punctuation():
    assert shorten("This is a test?!") == "Ths s  tst?!"
