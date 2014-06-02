"""
Event class that save the events
"""


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


class RecurringEvent(Event):
    def __init__(self, date, venue, hour, name, next_date):
        Event.__init__(self, date, venue, hour, name)
        self.next_date = next_date

    def next_event(self):
        return "Next time {0} will happen on {1}".format(self.name,
                                                         self.next_date)
