"""
Event class that save the events
"""

import datetime

def dateToStr(date):
    return "{0}.{1},{2}".format(date.day, date.month, date.year)

def timeToStr(time):
    return "{0}:{1}".format(time.hour, time.minute)

class Occurrence:
    def __init__(self, date, start = None, end = None):
        if start and end:
            self.start = datetime.datetime(
                    date.year,
                    date.mont,
                    date.day,
                    start.hour,
                    srart.minute)
            self.end = datetime.datetime(
                    date.year,
                    date.month,
                    date.day,
                    end.hour,
                    end.minute)
            self.all_day = False
        else:
            self.start = datetime.datetime(
                    date.year,
                    date.month,
                    date.day,
                    0,0)
            self.end = datetime.datetime(
                    date.year,
                    date.month,
                    date.day,
                    23,59)
            self.all_day = True
        self.duration = self.end- self.start
        self.date = date

    @property
    def year(self):
        return self.date.year

    @property
    def month(self):
        return self.date.month

    @property
    def day(self):
        return self.date.day

    @property
    def hour(self):
        return self.date.hour

    @property
    def minute(self):
        return self.date.minute

class Dayly:
    def __init__(self, start_date, step):
        self.start = start_date.toordinal()
        self.step = step

    def __str__(self):
        return "every {0} days starting {1}".format(self.step, dateToStr(start_date))


class Event:
    def __init__(self, date, venue, hour, name):
        self.date = date
        self.venue = venue
        self.hour = hour
        self.name = name

    def __str__(self):
        return "{0} will be held at {1}, on {2} at {3}".format(self.name,
                                                               self.venue,
                                                               self.date,
                                                               self.hour)



