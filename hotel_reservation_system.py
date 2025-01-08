class HotelReservationSystem:
    def __init__(self):
        # Hash table for reservations: key = "RoomNumber: Date", value = Customer Name
        self.room_reservations = {}
        # Hash table for customers: key = Customer Name, value = List of reservations
        self.customer_reservations = {}

    def book_room(self, room_number, date, customer_name):
        key = f"{room_number}: {date}"
        if key in self.room_reservations:
            print(f"Room {room_number} is already booked on {date} by {self.room_reservations[key]}.")
            return False
        # Add to room reservations
        self.room_reservations[key] = customer_name
        # Add to customer reservations
        if customer_name not in self.customer_reservations:
            self.customer_reservations[customer_name] = []
        self.customer_reservations[customer_name].append(key)
        print(f"Room {room_number} successfully booked on {date} for {customer_name}.")
        return True

    def check_availability(self, room_number, date):
        key = f"{room_number}: {date}"
        if key in self.room_reservations:
            print(f"Room {room_number} is booked on {date} by {self.room_reservations[key]}.")
            return False
        print(f"Room {room_number} is available on {date}.")
        return True

    def get_customer_reservations(self, customer_name):
        if customer_name not in self.customer_reservations:
            print(f"No reservations found for {customer_name}.")
            return []
        print(f"Reservations for {customer_name}: {self.customer_reservations[customer_name]}")
        return self.customer_reservations[customer_name]

    def cancel_reservation(self, room_number, date):
        key = f"{room_number}: {date}"
        if key not in self.room_reservations:
            print(f"No reservation found for Room {room_number} on {date}.")
            return False
        customer_name = self.room_reservations.pop(key)
        # Remove reservation from customer reservations
        self.customer_reservations[customer_name].remove(key)
        if not self.customer_reservations[customer_name]:  # Clean up if no reservations left
            del self.customer_reservations[customer_name]
        print(f"Reservation for Room {room_number} on {date} canceled.")
        return True

def main():
    hotel = HotelReservationSystem()

    # Adding reservations
    hotel.book_room(101, "20/09/2023", "Alice")
    hotel.book_room(102, "20/09/2023", "Bob")
    hotel.book_room(103, "21/09/2023", "Charlie")

    # Checking availability
    hotel.check_availability(101, "20/09/2023")
    hotel.check_availability(104, "20/09/2023")

    # Get reservations for a customer
    hotel.get_customer_reservations("Alice")
    hotel.get_customer_reservations("Bob")

    # Cancel a reservation
    hotel.cancel_reservation(101, "20/09/2023")

    # Verify cancellations
    hotel.check_availability(101, "20/09/2023")
    hotel.get_customer_reservations("Alice")

if __name__ == "__main__":
    main()
