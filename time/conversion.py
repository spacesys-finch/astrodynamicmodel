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
