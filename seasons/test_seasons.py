from seasons import get_minutes, inflect_time

def test_get_minutes():
    assert get_minutes("1999-01-01", today="2000-01-01") == 
