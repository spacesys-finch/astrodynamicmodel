import numpy as np
import datetime

class Clock:
    def __init__(self):


    # Evaluate the Julian Date from a Gregorian date input.
    # The Julian Date frame is the same frame as the input.
    def GregorianToJulianDate(self, gregorian):

        year = gregorian[0]
        month = gregorian[1]
        day = gregorian[2]
        hour = gregorian[3]
        min = gregorian[4]
        sec = gregorian[5]

        A = 367 * year
        B = (7 * (year + int((month + 9) / 12))) / 4
        C = (275 * month) / 9
        E = day + 1721013.5
        F = ((((sec / 60) + min) / 60) + hour) / 24

        JD = A - int(B) + int(C) + E + F

        return JD

    # Evaluate the Julian seconds from J2000 (TT).
    def GregorianToJSJ2000(self, gregorian):
        
        J2000 = GregorianToJulianDate(self, gregorian) - 2451545
        JS = J2000 / (1.1574*(10**(-5)))
        return JS


    # Evaluate the Julian Date from Julian Seconds from J2000 (TT).
    def JSJ2000ToJD(self, js_j2000):

        J2000 = js_j2000 * (1.1574*(10**(-5)))
        JD = J2000 + 2451545
        return JD


    # Evaluate Modified Julian Date.
    # The Modified Julian Date is the same frame as the JD input.
    def MJD(cls, JD):

        return JD - 2400000.5


    #Julian Date to Julian Centuries
    def JDToT(cls, jd):

        T = (jd - 2451545) / 36525
        return T


    #include extra perimter DUT1
    def UTCGregorianToUT1JSJ2000(self, gregorian, DUT1):
        UTCGregorian = datetime.datetime(gregorian[0], gregorian[1], gregorian[2], gregorian[3], gregorian[4], gregorian[5])
        UT1Gregorian = UTCGregorian + datetime.timedelta(seconds=DUT1)
        gregorian[4] = UT1Gregorian.minute
        gregorian[5] = UT1Gregorian.second
        UT1JSJ2000 = GregorianToJSJ2000(self, gregorian)
        return UT1JSJ2000


    def UTCGregoriantoTAIJD(self, gregorian_utc, DAT):
        TAIGegorian = gregorian_utc + DAT
        TAIJD = GregorianToJulianDate(self, TAIGegorian)
        return TAIJD


    def TAIstoTTs(self, tai_s):
        TT = tai_s + 32.184
        return TT


    def UTCGregorianToTTSeconds(self, gregorian_utc, DAT):
        TAIJD = UTCGregoriantoTAIJD(self, gregorian_utc, DAT)
        TAISeconds = TAIJD / (1.1574*(10**(-5)))
        TTSeconds = TAISeconds + 32.184
        return TTSeconds


    def UTCGregotianToTUT1(self, gregorian_utc):
        


    def GetdUT1fromGregorian(self, gregorian):


    # def GetEarthObservationParameter(self, mjd, param):


    def GetdATfromGregorian(self, gregorian):