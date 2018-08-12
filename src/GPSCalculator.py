class GPSCalculator(object):
    """
    GPSCalculator performs calculations on GPS coordinates

    This class assumes the earth has a radius of 6371km and
    that it is perfectly spherical.
    """

    EARTH_RADIUS_KM = 6371

    def __init__(self, math=None):
        """
            args
                math: a math module which implements sin, cos, sqrt,
                      asin. The standard math library will be used
                      by default.

        """
        self._math = math
        if self._math is None:
            import math
            self._math = math

    def distance(self, a, b):
        """
        Compute distance from a to b, using the haversine formula.

        args
            a,b: tuples of the form (latitude, longitude)
                 where latitude and longitude are given in radians
        """
        # Convention reminder:
        #   Phi = latitude
        #   Lamda = longitude

        # Alias for readibility
        m = self._math

        a_lat, a_lon = a
        b_lat, b_lon = b

        # latitude and longitude compute deltas
        latitude_delta = self._delta(a_lat, b_lat)
        longitude_delta = self._delta(a_lon, b_lon)

        # Compute inner terms
        first_term = m.sin(latitude_delta / 2) ** 2
        second_term = m.cos(a_lat) * m.cos(b_lat) * m.sin(longitude_delta / 2)
        inner = first_term + second_term

        # Compute delta sigma
        sigma_delta = 2 * m.asin(m.sqrt(inner))

        # Compute distance
        distance = self.EARTH_RADIUS_KM * sigma_delta

        return distance

    def _delta(self, x, y):
        """
        Compute the absolute difference of two values
        args
            x,y: numbers 
        """
        return abs(x - y)