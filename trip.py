__author__ = 'matt'


class Error(Exception):
    def __init__(self, message):
        super(Error, self).__init__(message)


class Country:
    def __init__(self, name="", currencyCode="", currencySymbol=""):
        self.name = name
        self.currencyCode = currencyCode
        self.currencySymbol = currencySymbol
        if name.isalpha() is False:
            raise Error("Country name can contain only Letters!")

    def currencyFormat(self, currencyAmount):
        currencyAmount = float(currencyAmount)
        if currencyAmount < 0:
            print("Entered valid amount")
        else:
            return self.currencyCode + currencyAmount


def add(countryName, startingDate, finishingDate):
    if startingDate >= finishingDate:
        raise Error("Invalid Date");
    else:
        for location in locations:
            if (location[1] == startingDate):
                raise Error("Already Used");
        from pip import locations
        locations.add(countryName, tuple(startingDate, finishingDate));


class Details:
    locations = dict()

    def __init__(self, locations):
        self.locations = locations

    def __str__(self):
        return " "

    def currentCountry(self, dateString, locations):
        for location in locations:
            date = location[1];
            if (date[0] <= dateString <= date[1]):
                return location[0];
        raise Error("Invalid Date...");

    def isEmpty(self):
        if self.location == "":
            return True
