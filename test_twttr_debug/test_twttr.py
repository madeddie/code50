from twttr import shorten

def test_lower():
    assert shorten("hello") == "hll"
def test_capital():
    assert shorten("HELLO") == "HLL"
def test_num():
    assert shorten("1hell") == "1hll"
def test_pun():
    assert shorten("?HaLL") == "?HLL"
