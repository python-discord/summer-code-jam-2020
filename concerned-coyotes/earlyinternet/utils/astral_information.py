import datetime

from astral import LocationInfo
from astral.moon import phase as moon_phase
from astral.sun import sunrise, sunset
from timezonefinder import TimezoneFinder


class AstralInformation:
    """Class that gives some astral information about
    a given location in geo coordinates.
    Example usage:
    ```
    # Berlin
    latitude = 52.520008
    longitude = 13.404954
    ast = AstralInformation(longitude, latitude)
    sunrise = ast.sunrise()
    ...
    ```
    """

    def __init__(
        self,
        longitude: float,
        latitude: float,
        date: datetime.datetime = datetime.datetime.utcnow()
    ) -> "AstralInformation":
        # To use the astral module, a LocationInfo object is required. This
        # however, requires a string of the timezone. That's where TimezoneFinder
        # comes in handy.
        tf = TimezoneFinder()
        timezone_name = tf.timezone_at(lng=longitude, lat=latitude)

        # Name and Region can be empty, as we can't guess that only based on the
        # coordinates. (We could, but too much work and not necessary)
        self.location = LocationInfo("", "", timezone_name, latitude, longitude)

        self.date = date

    def __repr__(self) -> str:
        return (
            f"<{self.__class__.__name__} "
            f"longitude={self.location.longitude} "
            f"latitude={self.location.latitude} "
            f"date={repr(self.date)}"
            ">"
        )

    @property
    def sunrise(self) -> datetime.datetime:
        return sunrise(observer=self.location.observer,
                       date=self.date)

    @property
    def sunset(self) -> datetime.datetime:
        return sunset(observer=self.location.observer,
                      date=self.date)

    @property
    def moon_phase(self) -> float:
        """Returns the moon phase.
        0..6.99     New moon
        7..13.99    First quarter
        14..20.99   Full moon
        21..27.99   Last quarter
        """
        return moon_phase(date=self.date)
