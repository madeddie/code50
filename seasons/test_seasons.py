from datetime import date
from seasons import get_minutes, inflect_time


today = date(2024, 2, 23)
def test_get_minutes():
    assert get_minutes("1999-01-01", today=today) == 13224960
    assert get_minutes("2023-02-23", today=today) == 525600

def test_inflect_time():
    assert inflect_time(13224960) == 'thirteen million, two hundred twenty-four thousand, nine hundred sixty'
    assert inflect_time(525600) == 'five hundred twenty-five thousand, six hundred'
