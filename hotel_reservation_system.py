class HotelReservationSystem:
    def __init__(self, size=10):
        # Initialize hash tables with a fixed number of buckets (for collisions)
        self.size = size
        self.room_reservations = [[] for _ in range(size)]  # Room reservations hash table
        self.customer_reservations = {}  # Customer reservations dictionary (no collision needed)

    def hash_function(self, key):
        # Simple hash function: sum of ASCII -> ord() values modulo table size
        return sum(ord(char) for char in key) % self.size

    def book_room(self, room_number, date, customer_name):
        key = f"{room_number}: {date}"
        index = self.hash_function(key)
        
        # Check if the room is already booked on the date
        for record in self.room_reservations[index]:
            if record[0] == key:
                print(f"Room {room_number} is already booked on {date} by {record[1]}.")
                return False

        # Add booking to room reservations
        self.room_reservations[index].append((key, customer_name))
        # Add to customer reservations
        if customer_name not in self.customer_reservations:
            self.customer_reservations[customer_name] = []
        self.customer_reservations[customer_name].append(key)
        print(f"Room {room_number} successfully booked on {date} for {customer_name}.")
        return True

    def check_availability(self, room_number, date):
        key = f"{room_number}: {date}"
        index = self.hash_function(key)
        
        # Check for key in the bucket
        for record in self.room_reservations[index]:
            if record[0] == key:
                print(f"Room {room_number} is booked on {date} by {record[1]}.")
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
        index = self.hash_function(key)
        
        # Find and remove the reservation from room reservations
        for record in self.room_reservations[index]:
            if record[0] == key:
                self.room_reservations[index].remove(record)
                customer_name = record[1]
                # Remove from customer reservations
                self.customer_reservations[customer_name].remove(key)
                if not self.customer_reservations[customer_name]:  # Clean up if no reservations left
                    del self.customer_reservations[customer_name]
                print(f"Reservation for Room {room_number} on {date} canceled.")
                return True
        print(f"No reservation found for Room {room_number} on {date}.")
        return False

    def display_room_reservations(self):
        print("Room Reservations:")
        for i, bucket in enumerate(self.room_reservations):
            print(f"Index {i}: {bucket}")


# Example Usage
hotel = HotelReservationSystem(size=5)  # Small size to demonstrate collisions

# Adding reservations
hotel.book_room(101, "20/09/2023", "Alice")
hotel.book_room(102, "20/09/2023", "Bob")
hotel.book_room(103, "21/09/2023", "Charlie")
hotel.book_room(101, "20/09/2023", "Dave")  # Collision for Room 101 on same date
hotel.book_room(103, "20/09/2023", "Eve")   # Collision with Room 103

# Display reservations with collisions
hotel.display_room_reservations()

# Checking availability
hotel.check_availability(101, "20/09/2023")
hotel.check_availability(104, "20/09/2023")

# Get reservations for a customer
hotel.get_customer_reservations("Alice")
hotel.get_customer_reservations("Eve")

# Cancel a reservation
hotel.cancel_reservation(101, "20/09/2023")

# Verify cancellations
hotel.check_availability(101, "20/09/2023")
hotel.get_customer_reservations("Alice")

# Display updated reservations
hotel.display_room_reservations()
