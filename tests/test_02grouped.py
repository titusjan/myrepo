""" Groups test functions together in a class

    Grouping tests in classes can be beneficial for the following reasons:
        * Test organization
        * Sharing fixtures for tests only in that particular class
        * Applying marks at the class level and having them implicitly apply to all tests

"""
import pytest

from myrepo.datetools import is_leap_year

class TestClassDemoInstance:

    # def test_is_leap_year_normal_use(self):
    #     assert is_leap_year(1971) == False
    #
    # def test_is_leap_year_true(self):
    #     assert is_leap_year(1976) == True

    def test_is_leap_year_centuries(self):
        assert is_leap_year(1800) == False

    def test_is_leap_year_four_centuries(self):
        assert is_leap_year(2000) == True

    def test_is_leap_year_bc(self):
        with pytest.raises(ValueError):
            assert is_leap_year(-10) == True

