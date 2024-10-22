#unit test for leap year logic
import leapYear
import pytest
def test_leapYear():

    assert leapYear.leapYear(1600) == True
    assert leapYear.leapYear(6400) == True

    return
def test_leapYearCornercases():
    assert leapYear.leapYear(2024) == True
    assert leapYear.leapYear(1744) == True
    assert leapYear.leapYear(2020) == True
    assert leapYear.leapYear(2108) == True
    assert leapYear.leapYear(1768) == True
    return

def test_typeError():
    with pytest.raises(TypeError):
        leapYear.leapYear("cat")