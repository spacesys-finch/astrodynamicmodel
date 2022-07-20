"""Unit Tests for ACSToolbox Foundation Package
"""

# Standard packages.
import numpy as np
import pytest as pytest

# ACSToolbox packages.
from acstoolbox.foundation import math
from acstoolbox.foundation import so3
from acstoolbox.foundation import conversion

# 1. so3.AxisAngle
def test_so3_euler_axis_rotation():
    # Use the same angle for all 3 tests.
    phi = -np.pi / 4
    c = np.cos(phi)
    s = np.sin(phi)

    # C3 Rotation.
    C3 = np.array(
        [
            [c, s, 0.0],
            [-s, c, 0.0],
            [0.0, 0.0, 1.0],
        ]
    )

    a = np.array([0.0, 0.0, 1.0])
    C = so3.AxisAngle(a, phi)
    assert np.allclose(C, C3)

    # C2 Rotation.
    C2 = np.array(
        [
            [c, 0.0, -s],
            [0.0, 1.0, 0.0],
            [s, 0.0, c],
        ]
    )

    a = np.array([0.0, 1.0, 0.0])
    C = so3.AxisAngle(a, phi)
    assert np.allclose(C, C2)

    # C1 Rotation.
    C1 = np.array(
        [
            [1.0, 0.0, 0.0],
            [0.0, c, s],
            [0.0, -s, c],
        ]
    )

    a = np.array([1.0, 0.0, 0.0])
    C = so3.AxisAngle(a, phi)
    assert np.allclose(C, C1)


# 2. so3.C
def test_so3_C():
    # Use the same angle for all 3 tests.
    phi_deg = 45
    phi_rad = np.radians(45)

    # Principal axis rotation about axis 1.
    C1 = so3.AxisAngle(np.array([1.0, 0.0, 0.0]), phi_rad)
    assert np.allclose(so3.C(1, phi_deg), C1)

    # Principal axis rotation about axis 2.
    C2 = so3.AxisAngle(np.array([0.0, 1.0, 0.0]), phi_rad)
    assert np.allclose(so3.C(2, phi_deg), C2)

    # Principal axis rotation about axis 3.
    C3 = so3.AxisAngle(np.array([0.0, 0.0, 1.0]), phi_rad)
    assert np.allclose(so3.C(3, phi_deg), C3)

    # Principal axis rotation about erroneous axis.
    try:
        C = so3.C(4, phi_deg)
    except AssertionError:
        print("Exception caught constructing principal rotation")
        # raise


# 3. test Spherical to Cartesian
def test_spherical_to_cartesian():

    # use a spherical coordinate value
    spherical = np.array([5, 2.45, 3.14])
    cartessian = conversion.SphericaltoCartesian(spherical)

    # cartesian coordinate
    cartesian_test = [-3.18881947, 0.00507869, -3.85115627]
    assert np.allclose(cartessian, cartesian_test)


# 4. test Cartesian to Spherical
def test_cartesian_to_spherical():

    # cartesian coordinate value
    cartesian = np.array([1, 2, 3])
    spherical = conversion.CartesiantoSpherical(cartesian)

    # spherical coordinate test
    spherical_test = [3.74165739, 0.64052231, 1.10714872]
    assert np.allclose(spherical, spherical_test)
