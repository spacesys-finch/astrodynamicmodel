# Standard packages.
import numpy as np


def SphericaltoCartesian(Spherical):
    R = Spherical[0]
    theta = Spherical[1]
    phi = Spherical[2]
    x = R * np.sin(theta) * np.cos(phi)
    y = R * np.sin(theta) * np.sin(phi)
    z = R * np.cos(theta)
    return np.array([x, y, z])


def CartesiantoSpherical(Cartesian):
    x = Cartesian[0]
    y = Cartesian[1]
    z = Cartesian[2]
    R = np.sqrt((x**2) + (y**2) + (z**2))
    theta = np.arccos(z / np.sqrt((x**2) + (y**2) + (z**2)))
    phi = np.arctan(y / x)
    return np.array([R, theta, phi])
