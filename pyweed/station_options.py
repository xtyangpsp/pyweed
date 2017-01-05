from options import Options, DateOption, FloatOption, Option


class StationOptions(Options):

    time_choice = Option(hidden=True)
    TIME_RANGE = 'timeBetweenRadioButton'
    TIME_EVENTS = 'timeDuringEventsRadioButton'

    starttime = DateOption()
    endtime = DateOption()

    network = Option()
    station = Option()
    location = Option()
    channel = Option()

    location_choice = Option(hidden=True)
    LOCATION_BOX = 'locationRangeRadioButton'
    LOCATION_POINT = 'locationDistanceFromPointRadioButton'
    LOCATION_EVENTS = 'locationDistanceFromEventsRadioButton'

    minlatitude = FloatOption()
    maxlatitude = FloatOption()
    minlongitude = FloatOption()
    maxlongitude = FloatOption()

    latitude = FloatOption()
    longitude = FloatOption()
    minradius = FloatOption()
    maxradius = FloatOption()

    def get_obspy_options(self):
        exclude = set()
        if self.time_choice != self.TIME_RANGE:
            exclude.update(['starttime', 'endtime'])
        if self.location_choice != self.LOCATION_BOX:
            exclude.update(['minlatitude', 'maxlatitude', 'minlongitude', 'maxlongitude'])
        if self.location_choice != self.LOCATION_POINT:
            exclude.update(['latitude', 'longitude', 'minradius', 'maxradius'])

        keys = [k for k in self.keys(hidden=False) if k not in exclude]
        return self.get_options(keys=keys)

