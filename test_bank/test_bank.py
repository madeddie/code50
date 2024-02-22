from bank import value

def test_hello():
    assert value("hello") == 0

def test_hello_upper():
    assert value("HELLO") == 0

def test_start_with_h():
    assert value("hi") == 20
    assert value("Hi") == 20
    assert value("Hobo") == 20

def test_no_start_with_h():
    assert value("abc") == 100
    assert value("Allo") == 100
    assert value("123") == 100
