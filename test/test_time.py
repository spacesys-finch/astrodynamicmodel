""" this file will test everything related to time"""


from 
astrodynamicmodel.time import jdconversion_version2

import numpy as np
import pytest as pytest



# UTCtoJDUTC
# Convert Gregorian to Julian Date.
def test_gregorian_to_julian_date():
    # J2000 (January 1, 2000 12hh00mm00ss).
    gregorian_j2000 = [2000, 1, 1, 12, 0, 0]

    # Initialize clock and convert Gregorian date.

    time = jdconversion_version2.GregorianToJulianDate(gregorian_j2000)
    print(time)

def test_LST():
    clock = Clock()
    # calculate LST time
    gregorian = [1992, 8, 20, 12, 14, 0]
    lamda = -104
    LST = clock.LSTime(gregorian, lamda)
    # example LST time
    LST_test = 48.578787886
    # test
    assert LST == pytest.approx(LST_test, 1e-2)

if __name__ == "__main__":
    test_gregorian_to_julian_date()
