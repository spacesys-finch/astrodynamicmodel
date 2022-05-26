import numpy as np
import pytest as pytest



# UTCtoJDUTC
# Convert Gregorian to Julian Date.
def test_gregorian_to_julian_date():
    # J2000 (January 1, 2000 12hh00mm00ss).
    gregorian_j2000 = [2000, 1, 1, 12, 0, 0]

    # Initialize clock and convert Gregorian date.
    clock = Clock()
    assert clock.GregorianToJulianDate(gregorian_j2000) == JD_J2000