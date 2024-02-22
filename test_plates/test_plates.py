from plates import is_valid

def test_start_with_2_letters():
    assert is_valid("AB123") == True
    assert is_valid("A123") == False

def test_max6_min2():
    assert is_valid("AB1234") == True
    assert is_valid("AB12345") == False
    assert is_valid("A") == False

def test_numbers_at_end():
    assert is_valid("AB123") == True
    assert is_valid("A123B") == False
    assert is_valid("123AB") == False

def test_first_number_0():
    assert is_valid("AB123") == True
    assert is_valid("AB012") == False

def test_nothing_but_alnum():
    assert is_valid("AB123") == True
    assert is_valid("AB123!") == False
    assert is_valid("AB 123") == False
    assert is_valid("AB12.3") == False
    assert is_valid("AB,123") == False
