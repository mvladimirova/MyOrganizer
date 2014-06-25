import event
import unittest
from datetime import datetime


class EventTest(unittest.TestCase):
    def test_event_instance(self):
        ev = event.Event("18.03.2014", "FMI", "18:00", "izpit")
        self.assertEqual(ev.date, datetime(2014, 3, 18, 0, 0))
        self.assertEqual(ev.venue, "FMI")
        self.assertEqual(ev.hour, "18:00")
        self.assertEqual(ev.name, "izpit")

    def test_to_string(self):
        ev = event.Event("18.3.2014", "FMI", "18:00", "izpit")
        self.assertEqual(str(ev),
                         "izpit will be held at FMI, on 18.3.2014 at 18:00")


class DaylyEventTests(unittest.TestCase):
    def test_dayly_instance(self):
        dayly = event.Dayly("23.12.2014", "home", "08:00", "write code", 1)
        self.assertEqual(dayly.date, datetime(2014, 12, 23, 0, 0))
        self.assertEqual(dayly.venue, "home")
        self.assertEqual(dayly.hour, "08:00")
        self.assertEqual(dayly.name, "write code")
        self.assertEqual(dayly.step, 1)

    def test_dayly_str(self):
        dayly = event.Dayly("23.12.2014", "home", "08:00", "write code", 1)
        self.assertEqual(str(dayly),
                         "every 1 day/s starting 23.12.2014")

    def test_occurs_on_date(self):
        dayly = event.Dayly("23.12.2014", "home", "08:00", "write code", 1)
        self.assertEqual(dayly.occurs_on_date("24.12.2014"), True)

        dayly2 = event.Dayly("23.12.2014", "home", "08:00", "write code", 2)
        self.assertEqual(dayly2.occurs_on_date("24.12.2014"), False)


class WeeklyEventTest(unittest.TestCase):
    def test_weekly_instance(self):
        w = event.Weekly("FMI", "18:00", "python", 1)
        self.assertEqual(w.venue, "FMI")
        self.assertEqual(w.hour, "18:00")
        self.assertEqual(w.name, "python")
        self.assertEqual(w.days, {1})

    def test_weekly_str(self):
        w = event.Weekly("FMI", "18:00", "python", 1)
        self.assertEqual(str(w), "every monday")
        w1 = event.Weekly("FMI", "18:00", "python", 1, 3)
        self.assertEqual(str(w1), "every monday, wednesday")

    def test_occurs_on_date(self):
        w = event.Weekly("FMI", "18:00", "python", 1)
        self.assertEqual(w.occurs_on_date("30.6.2014"), True)
        self.assertEqual(w.occurs_on_date("1.7.2014"), False)
        w1 = event.Weekly("FMI", "18:00", "python", 1, 3)
        self.assertEqual(w1.occurs_on_date("29.6.2014"), False)
        self.assertEqual(w1.occurs_on_date("25.6.2014"), True)
        self.assertEqual(w1.occurs_on_date("30.6.2014"), True)


class MonthlyEventTest(unittest.TestCase):
    def test_first_monthly_instance(self):
        m = event.Monthly(18, "mom's birthday", 11)
        self.assertEqual(m.day, 18)
        self.assertEqual(m.name, "mom's birthday")
        self.assertEqual(m.month, 11)

    def test_second_monthly_instance(self):
        m = event.Monthly(18, "another month since we are together")
        self.assertEqual(m.day, 18)
        self.assertEqual(m.name, "another month since we are together")
        self.assertEqual(m.month, None)

    def test_first_str(self):
        m = event.Monthly(18, "mom's birthday", 11)
        self.assertEqual(str(m), "18-th of each november")

    def test_second_str(self):
        m = event.Monthly(18, "another month since we are together")
        self.assertEqual(str(m), "18-th of each month")

    def test_first_occurs_on_date(self):
        m = event.Monthly(18, "mom's birthday", 11)
        self.assertEqual(m.occurs_on_date("18.11.2015"), True)


if __name__ == '__main__':
    unittest.main()
