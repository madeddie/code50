import pytest

from fuel import convert, gauge

def test_convert_fail_int():
    with pytest.raises(ValueError):
        convert("1/cat")

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
