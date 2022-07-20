import sys
sys.path.append("C:\\Users\\khang\\OneDrive\\Music\\Documents\\ADCS\\simulation")

# ACSToolbox packages.
from acstoolbox.ephemerides.IGRF import igrf
import os

# Standard packages.
import numpy as np
import pytest as pytest

def test_igrf():
    R = np.linalg.norm([859.52248524, -4541.5945528, 4380.34474178])
    theta = -79.2832
    phi = 43.6532
    year = 2022
    filepath = "IGRF13.txt"
    IGRF = igrf(filepath)
    magneticfield = IGRF.IGRFinECEF(R, theta, phi, year)
    print(magneticfield)


if __name__ == "__main__":
    test_igrf()