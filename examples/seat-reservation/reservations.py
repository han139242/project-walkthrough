"""Small in-memory example for a project walkthrough."""


class Reservations:
    def __init__(self):
        self.bookings = []
        self._receipts = {}

    def reserve(self, person, seat, request_id):
        if request_id in self._receipts:
            return self._receipts[request_id]

        result = {"status": "accepted", "seat": seat}
        self.bookings.append((person, seat))
        self._receipts[request_id] = result
        return result
