import unittest
from hotel_reservation_system import HotelReservationSystem

class TestHotelReservationSystem(unittest.TestCase):

    def setUp(self):
        self.hotel = HotelReservationSystem(size=5)

    def test_hash_function(self):
        self.assertEqual(self.hotel.hash_function("Room 101: 20/09/2023"), 
                         sum(ord(c) for c in "Room 101: 20/09/2023") % 5)
        self.assertEqual(self.hotel.hash_function("Room 102: 20/09/2023"), 
                         sum(ord(c) for c in "Room 102: 20/09/2023") % 5)

    def test_book_room(self):
        # Book a room and confirm success
        result = self.hotel.book_room(101, "20/09/2023", "Alice")
        self.assertTrue(result)

        # Try booking the same room on the same date
        result = self.hotel.book_room(101, "20/09/2023", "Bob")
        self.assertFalse(result)

    def test_check_availability(self):
        # Book a room
        self.hotel.book_room(101, "20/09/2023", "Alice")
        # Check availability for the same room
        self.assertFalse(self.hotel.check_availability(101, "20/09/2023"))
        # Check availability for another room
        self.assertTrue(self.hotel.check_availability(102, "20/09/2023"))

    def test_cancel_reservation(self):
        # Book a room and cancel it
        self.hotel.book_room(101, "20/09/2023", "Alice")
        result = self.hotel.cancel_reservation(101, "20/09/2023")
        self.assertTrue(result)

        # Check availability after cancellation
        self.assertTrue(self.hotel.check_availability(101, "20/09/2023"))

        # Try cancelling a non-existent reservation
        result = self.hotel.cancel_reservation(101, "21/09/2023")
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
