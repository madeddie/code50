import pytest

from jar import Jar


def test_init():
    jar = Jar()
    assert jar.capacity == 12
    jar = Jar(capacity=15)
    assert jar.capacity == 15
    with pytest.raises(ValueError):
        jar = Jar(capacity=-1)

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar(capacity=12)
    jar.deposit(3)
    assert jar.size == 3
    with pytest.raises(ValueError):
        jar.deposit(10)


def test_withdraw():
    jar = Jar(capacity=5)
    jar.deposit(5)
    jar.withdraw(2)
    assert jar.size == 3
    with pytest.raises(ValueError):
        jar.withdraw(4)
