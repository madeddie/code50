import pytest

from fuel import convert, gauge

""" def test_convert():
    assert convert("2/3") == 67
    with pytest.raises(ValueError):
        assert convert("cat/dog")
    with pytest.raises(ValueError):
        assert convert("3/2")
    with pytest.raises(ZeroDivisionError):
        assert convert("0/0") """


def test_convert_fail_int():
    with pytest.raises(ValueError):
        convert("cat/dog")

def test_convert_fail_x_gt_y():
    with pytest.raises(ValueError):
        convert("2/1")

def test_convert_y_0():
    with pytest.raises(ZeroDivisionError):
        convert("0/0")

def test_gauge_empty():
    assert gauge(1) == "E"
    assert gauge(0) == "E"

def test_gauge_full():
    assert gauge(100) == "F"
    assert gauge(99) == "F"

def test_gauge_percentage():
    assert gauge(50) == "50%"
    assert gauge(3) == "3%"
    assert gauge(98) == "98%"
