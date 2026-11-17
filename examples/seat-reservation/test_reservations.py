import unittest

from reservations import Reservations


class ReservationsTest(unittest.TestCase):
    def test_sequential_retry_keeps_one_booking(self):
        reservations = Reservations()
        first = reservations.reserve("reader", "A1", "request-1")
        second = reservations.reserve("reader", "A1", "request-1")

        self.assertEqual(first, second)
        self.assertEqual(reservations.bookings, [("reader", "A1")])

    def test_different_request_ids_keep_distinct_bookings(self):
        reservations = Reservations()
        reservations.reserve("reader", "A1", "request-1")
        reservations.reserve("reader", "A2", "request-2")

        self.assertEqual(reservations.bookings, [("reader", "A1"), ("reader", "A2")])
