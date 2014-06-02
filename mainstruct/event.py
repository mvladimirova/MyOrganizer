"""
Event class that save the events
"""
from datetime import datetime

def dateToStr(date):
    return "{0}.{1}.{2}".format(date.day, date.month, date.year)

def timeToStr(time):
    return "{0}:{1}".format(time.hour, time.minute)


class Dayly:
    def __init__(self, start_date, step):
        startDate = datetime.strptime(start_date, '%d  %b %Y')
        self.start = startDate
        self.step = step

    def __str__(self):
        return "every {0} days starting {1}".format(self.step, dateToStr(self.start))
    
    def occursOnDate(self, date):
        Date = datetime.strptime(date, '%d %b %Y')
        return Date >= self.start

daynames = ["monday","tuesday","wednesday","thursday",
            "friday", "saturday", "sunday"]

class Weekly:

    def __init__(self, *days):
        self.days = set(days)

    def __str__(self):
        return "every " + ", ".join((daynames[day] for day in self.days))

    def occursOndate(self, date):
        Date = datetime.strptime(date, '%d %b %Y')
        return Date.weekday() in self.days

monthnames = ["january", "february", "march",
              "april", "may", "june", "july",
              "august", "september", "october",
              "november", "december"]

class Monthly:
    def __init__(self, date, month = None):
        occur_date = datetime.strptime(date, '%d')
        self.day = occur_date
        self.month = month

    def __str__(self):
        if not self.month:
            return "{0} of each month".format(self.day)
        else:
            return "{0} of each {1}".format(self.day, monthnames[self.month])

    def occursOnDate(self, date):
        Date = datetime.strptime(date, '%d %b %Y')
        if not self.month:
            return Date.day == self.day
        else:
            return (Date.day == self.day) and (Date.month == self.month)


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



