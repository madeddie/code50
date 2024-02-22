from numb3rs import validate


def test_correct():
    assert validate('1.2.3.4') == True
    assert validate('127.0.0.1') == True
    assert validate('255.255.255.255') == True

def test_incorrect():
    assert validate('512.512.512.512') == False
    assert validate('1.2.3.1000') == False
    assert validate('cat') == False
    assert validate('1.256.1.1') == False
