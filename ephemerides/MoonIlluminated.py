from acstoolbox.time.clock import Clock
from acstoolbox.ephemerides.moon import Moon


if __name__ == "__main__":
    clock = Clock()
    moon = Moon(clock)
    # Evaluate the moon phase on April 3, 2020 at 0:00 UTC
    gregorian_utc = [2020, 4, 3, 0, 0, 0]
    phase = moon.PercentageMoonIlluminated(gregorian_utc)
    print("Surface of the moon that is illuminated: "phase)
    # expected outout
    phase_test = 66.7277