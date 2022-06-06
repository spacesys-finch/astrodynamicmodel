import numpy as np

class Clock:
    def __init__(self):


    # Evaluate the Julian Date from a Gregorian date input.
    # The Julian Date frame is the same frame as the input.
    def GregorianToJulianDate(self, gregorian):


    # Evaluate the Julian seconds from J2000 (TT).
    def GregorianToJSJ2000(self, gregorian):


    # Evaluate the Julian Date from Julian Seconds from J2000 (TT).
    def JSJ2000ToJD(self, js_j2000):


    # Evaluate Modified Julian Date.
    # The Modified Julian Date is the same frame as the JD input.
    def MJD(cls, JD):


    def JDToT(cls, jd):


    def UTCGregorianToUT1JSJ2000(self, gregorian):


    def UTCGregoriantoTAIJD(self, gregorian_utc):


    def TAIstoTTs(self, tai_s):


    def UTCGregorianToTTSeconds(self, gregorian_utc):


    def UTCGregotianToTUT1(self, gregorian_utc):


    def GetdUT1fromGregorian(self, gregorian):


    def GetEarthObservationParameter(self, mjd, param):


    def GetdATfromGregorian(self, gregorian):

    def GMST(self, gregorian):
        c_ut1 = self.UTCGregotianToTUT1(gregorian)
        GMST = (
            67310.54841
            + (3155760000 + 8640184.812866) * c_ut1
            + 0.093104 * (c_ut1**2)
            - 0.0000062 * (c_ut1**3)
        ) % 86400
        GMST = GMST / 240
        if GMST < 0:
            GMST = 360 - GMST
        return GMST


    def LSTime(self, gregorian, lamda):
        GMST = self.GMST(gregorian)
        LST = GMST + lamda
        return LST
