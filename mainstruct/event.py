"""
A main class Event that will be the base for the Dayly and Monthly
classes
"""

from datetime import datetime


def date_to_str(date):
    return "{0}.{1}.{2}".format(date.day, date.month, date.year)


def time_to_str(time):
    return "{0}:{1}".format(time.hour, time.minute)

class Event:
    """
    Class for one time events. Used as a base class for the other types
    """
    def __init__(self, date, venue, hour, name):
        """
        Constructor for event class
        """
        self.date = datetime.strptime(date, '%d.%m.%Y')
        self.venue = venue
        self.hour = hour
        self.name = name

    def __str__(self):
        """
        Returns a string when the event will happen
        """
        return "{0} will be held at {1}, on {2} at {3}".format(self.name,
                                                               self.venue,
                                                               date_to_str(self.date),
                                                               self.hour)

class Dayly(Event):
    """
    Class for events that are every day
    """
    def __init__(self, date, venue, hour, name, step):
        self.step = step
        super(Dayly, self).__init__(date, venue, hour, name)

    def __str__(self):
        return "every {0} day/s starting {1}".format(self.step,
                                                     date_to_str(self.date))

    def occurs_on_date(self, date):
        """
        Checks if the event will happen on a current date
        """
        Date = (datetime.strptime(date, '%d.%m.%Y')).toordinal()
        start_date = self.date.toordinal()
        return Date >= start_date and (((Date - start_date) % self.step) == 0)

day_names = ["monday", "tuesday", "wednesday", "thursday",
             "friday", "saturday", "sunday"]


class Weekly:
    """
    Class for weekly events
    """
    def __init__(self, venue, hour, name, *days):
        self.days = set(days)
        self.venue = venue
        self.hour = hour
        self.name = name

    def __str__(self):
        return "every " + ", ".join((day_names[day] for day in self.days))

    def occurs_on_date(self, date):
        Date = datetime.strptime(date, '%d.%m.%Y')
        return Date.weekday() in self.days

month_names = ["january", "february", "march",
               "april", "may", "june", "july",
               "august", "september", "october",
               "november", "december"]

class Monthly:
    """
    Class for monthly event. If enter a month when creating the event
    it will be saved only for that month
    """
    def __init__(self, day, name, month=None):
        self.day = day
        self.name = name
        if(month != None):
            self.month = month
        else:
            self.month = None

    def __str__(self):
        if not self.month:
            return "{0}-th of each month".format(self.day)
        else:
            return "{0}-th of each {1}".format(self.day, month_names[self.month-1])

    def occurs_on_date(self, date):
        Date = datetime.strptime(date, '%d.%m.%Y')
        if not self.month:
            return Date.day == self.day
        else:
            return (Date.day == self.day) and (Date.month == self.month)
