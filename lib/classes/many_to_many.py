class Band:
    def __init__(self, name, hometown):
        self.name = name
        self.hometown = hometown
        self._concerts = []

    def concerts(self):
        """Return all concerts this band has played."""
        return self._concerts

    def venues(self):
        """Return all unique venues where this band has played."""
        return list({concert.venue for concert in self._concerts})

    def play_in_venue(self, venue, date):
        """Create a concert with this band at the given venue on the given date."""
        concert = Concert(date=date, band=self, venue=venue)
        self._concerts.append(concert)
        venue._concerts.append(concert)
        Concert.all.append(concert)   
        return concert

    def all_introductions(self):
        """Return a list of introductions for all concerts."""
        return [concert.introduction() for concert in self._concerts]


class Concert:
    all = []

    def __init__(self, date, band, venue):
        # Basic validation for date
        if not isinstance(date, str) or len(date) == 0:
            raise Exception("Date must be a non-empty string")
        if not isinstance(band, Band):
            raise Exception("band must be a Band instance")
        if not isinstance(venue, Venue):
            raise Exception("venue must be a Venue instance")

        self._date = date
        self._band = band
        self._venue = venue

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise Exception("Date must be a non-empty string")
        self._date = value

    @property
    def band(self):
        return self._band

    @band.setter
    def band(self, value):
        if not isinstance(value, Band):
            raise Exception("band must be a Band instance")
        self._band = value


    @property
    def venue(self):
        return self._venue

    @venue.setter
    def venue(self, value):
        if not isinstance(value, Venue):
            raise Exception("venue must be a Venue instance")
        self._venue = value

    def hometown_show(self):
        """Return True if concert is in band's hometown, else False."""
        return self.venue.city == self.band.hometown
    def introduction(self):
        """Return the band's introduction message for this concert."""
        return f"Hello {self.venue.city}!!!!! We are {self.band.name} and we're from {self.band.hometown}"


class Venue:
    def __init__(self, name, city):
        if not isinstance(name, str) or len(name) == 0:
            raise Exception("Name must be a non-empty string")
        if not isinstance(city, str) or len(city) == 0:
            raise Exception("City must be a non-empty string")

        self._name = name
        self._city = city
        self._concerts = [] 

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise Exception("Name must be a non-empty string")
        self._name = value

    @property
    def city(self):
        return self._city
    @city.setter
    def city(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise Exception("City must be a non-empty string")
        self._city = value

    def concerts(self):
        """Return all concerts held at this venue."""
        return self._concerts

    def bands(self):
        """Return all unique bands that have played at this venue."""
        return list({concert.band for concert in self._concerts})

  