class Location(object):
    """
    A gps location.
    """

    def __init__(self, latitude, longitude, math=None):
        """
        Create a location, based on a given latitude and
        longitude.

        args
            latitude, in degrees
            longitude, in degrees
            math, a math module which implements .radians()
        """
        self._latitude = latitude
        self._longitude = longitude
        self._math = math

        if self._math is None:
            import math
            self._math = math

    def _to_radians(self, x):
        """ Convert x to radians"""
        return self._math.radians(x)

    @property
    def degrees(self):
        """
        Return the location as a tuple of the form
        (latitude, longitude) where latitude and longitude
        are in degrees.
        """
        return (self._latitude, self._longitude)

    @property
    def radians(self):
        """
        Return the location as a tuple of the form
        (latitude, longitude) where latitude and longitude
        are in radians.
        """
        latitude = self._to_radians(self._latitude)
        longitude = self._to_radians(self._longitude)
        return (latitude, longitude)
