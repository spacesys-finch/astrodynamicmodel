# ACSToolbox packages.
from acstoolbox.time.clock import Clock
from acstoolbox.ephemerides.moon import Moon

# Standard packages.
import numpy as np
import pytest as pytest

# Evaluate moon vector from UTC in KM
if __name__ == "__main__":
    clock = Clock()
    moon = Moon(clock)

    # Evaluate the moon vector from April 28, 1994, 0:00 UTC
    gregorian_utc = [1994, 4, 28, 0, 0, 0]
    m_vector = moon.VectorFromUTCinKM(gregorian_utc)