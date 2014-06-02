import unittest
import event


class EventTest(unittest.TestCase):
    def test_event_instance(self):
        ev = event.Event("18.03.2014", "FMI", "18:00", "izpit")
        self.assertEqual(ev.date, "18.03.2014")
        self.assertEqual(ev.venue, "FMI")
        self.assertEqual(ev.hour, "18:00")
        self.assertEqual(ev.name, "izpit")

    def test_to_string(self):
        ev = event.Event("18.03.2014", "FMI", "18:00", "izpit")
        self.assertEqual(str(ev),
                         "izpit will be held at FMI, on 18.03.2014 at 18:00")


if __name__ == '__main__':
    unittest.main()
