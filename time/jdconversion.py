# converting from geogrian date to julian date
def A(year, month):
    return (7 * (year + int((month + 9) / 12))) / 4


def B(month):
    return (275 * month) / 9


def C(day):
    return day + 1721013.5


def E(hour, min, sec):
    return ((((sec / 60) + min) / 60) + hour) / 24


def JD(year, month, day, hour, min, sec):
    JD = (
        367 * year
        - (int)(A(year, month))
        + (int)(B(month))
        + C(day)
        + E(hour, min, sec)
    )
    return JD
