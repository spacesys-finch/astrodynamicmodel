# ACSToolbox packages.
from astrodynamicmodel.time.clock import Clock
from astrodynamicmodel.ephemerides.sun import Sun
from astrodynamicmodel.ephemerides.moon import Moon

# Standard packages.
import numpy as np
import pytest as pytest

# TODO
# 1. Evaluate unit sun vector from JS from J2000 (in TT, not UTC)
# 2. Updated test_sun_vector_from_utc using current Astronomical Almanac

# 1. Evaluate unit sun vector from UTC Gregorian date.
def test_sun_vector_from_utc():
    clock = Clock()
    sun = Sun(clock)

    # Evaluate the sun vector in the MOD frame on 2 April 2006 00hh00mm00ss.
    epoch_gregorian_utc = [2006, 4, 2, 0, 0, 0]
    s_mod = sun.GetUnitMODPositionFromUTC(epoch_gregorian_utc)

    # Astronomical Almanac (ICRS).
    s_mod_almanac = np.array([0.9776782, 0.1911521, 0.0828717])

    # Test the accuracy of each unit vector component.
    assert s_mod == pytest.approx(s_mod_almanac, 1e-2)

    # Test the angular difference of the unit sun vector.
    us_mod_almanac = s_mod_almanac / np.linalg.norm(s_mod_almanac)
    dphi = np.arccos(np.dot(s_mod, us_mod_almanac)) / np.pi * 180.0
    assert dphi < 1e-1


# 2. Evaluate moon vector from Julian Second from the J2000 epoch in ER
def test_moon_vector_from_tt():

    clock = Clock()
    moon = Moon(clock)
    # Evaluate the moon vector from April 28, 1994, 0:00 UTC
    gregorian_utc = [1994, 4, 28, 0, 0, 0]
    jsj2000_tt = clock.GregorianToJSJ2000(gregorian_utc)
    m_vector = moon.VectorFromTT(jsj2000_tt)

    # Astronomical Almanac (ICRS).
    m_mod_almanac = np.array([-21.0469963, -48.84993696, -19.86376033])

    assert m_vector == pytest.approx(m_mod_almanac, 1e-2)


# 3. Evaluate moon vector from UTC in ER
def test_moon_vector_from_utc():

    clock = Clock()
    moon = Moon(clock)

    # Evaluate the moon vector from April 28, 1994, 0:00 UTC
    gregorian_utc = [1994, 4, 28, 0, 0, 0]

    m_vector = moon.VectorFromUTC(gregorian_utc)

    # Astronomical Almanac (ICRS).
    m_mod_almanac = np.array([-21.0469963, -48.84993696, -19.86376033])

    assert m_vector == pytest.approx(m_mod_almanac, 1e-2)


# 4. Evaluate moon vector from UTC in KM
def test_moon_vector_in_km():
    clock = Clock()
    moon = Moon(clock)

    # Evaluate the moon vector from April 28, 1994, 0:00 UTC
    gregorian_utc = [1994, 4, 28, 0, 0, 0]
    m_vector = moon.VectorFromUTCinKM(gregorian_utc)

    # Example Value:
    example_vec = [-134241.192, -311571.349, -126693.681]
    assert m_vector == pytest.approx(example_vec, 1e-2)


# 5. Evaluate normalize moon vector from UTC
def test_moon_vec_normal():
    clock = Clock()
    moon = Moon(clock)
    # Evaluate the moon vector from April 28, 1994, 0:00 UTC
    gregorian_utc = [1994, 4, 28, 0, 0, 0]
    m_vector = moon.VectorFromUTC(gregorian_utc)
    moon_vector = m_vector / np.linalg.norm(m_vector)
    # Check with the new fuction
    moonvector = moon.MoonVectorNormal(gregorian_utc)
    assert moon_vector == pytest.approx(moonvector, 1e-2)


# 6. Evaluate moon phase from April 3, 2020 at 0:00 UTC
def test_moon_phase():
    clock = Clock()
    moon = Moon(clock)
    # Evaluate the moon phase on April 3, 2020 at 0:00 UTC
    gregorian_utc = [2020, 4, 3, 0, 0, 0]
    phase = moon.PercentageMoonIlluminated(gregorian_utc)
    # Test moon phase
    phase_test = 66.7277
    assert phase == pytest.approx(phase_test, 1e-2)
