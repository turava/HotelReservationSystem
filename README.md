# Hotel Room Reservation System

## Description
This project implements a reservation system for a hotel using hash tables. It allows adding reservations, checking room availability, retrieving bookings by customer name, and canceling specific reservations.

## Features
- **Book Room:** Add a reservation with the customer's name, date, and room number.
- **Check Reservation by Name:** Check if a room is available on a specific date.
- **Retrieve Room Availability:** Retrieve all bookings for a specific customer.
- **Cancel Reservation:** Cancel a reservation for a specific room and date.

## Data Structure
- A hash table where the key is a combination of the room number and date (e.g., "Room 101: 20/09/2023") and the value is the customer's name.
- A second hash table where the key is the customer's name and the value is a list of their bookings.

## Sample Data
- At least 5 rooms and 3 different dates for bookings.
- At least 3 different customers with at least 1 booking each.

## Additional Questions
1. What happens if two customers try to book the same room on the same date at the same time?
2. How can you ensure that all bookings for a customer with multiple reservations on different dates are efficiently retrieved?
3. How would you handle last-minute reservation cancellations or no-shows?

## Tips
- Remember to handle potential collisions in your hash table and think about the system's efficiency as more and more bookings are added.

# Understanding Hash Tables

## What Are Hash Tables?

A **hash table** is a data structure that maps **keys** to **values**, allowing for fast data retrieval. It uses a **hash function** to compute an index (or "hash value") where the data is stored in an array. This makes hash tables efficient for operations like lookups, insertions, and deletions.

---

## Key Concepts of Hash Tables

### 1. **Hash Function**
- Converts a key (e.g., a string or number) into an index within the table.
- Ensures the same key always maps to the same index.
- Example:
  - Key: `"Room 101: 20/09/2023"`
  - Hash Function Output: `42` (index)

### 2. **Buckets**
- The table contains slots or buckets, where each bucket corresponds to an index.
- Each bucket can hold one or more key-value pairs.

### 3. **Collisions**
- Occur when two keys produce the same index.
- Handled using techniques like:
  - **Chaining**: Store multiple key-value pairs at the same index in a list or linked list.
  - **Open Addressing**: Search for the next available slot.

### 4. **Efficiency**
- Hash tables provide an **average time complexity of O(1)** for:
  - Insertions
  - Deletions
  - Lookups
- In the worst-case scenario (e.g., many collisions), performance can degrade to **O(n)**.

---

## Example Analogy: Hotel Reservations
Imagine a hotel receptionist managing reservations:
1. The receptionist uses a chart (hash function) to decide which pigeonhole (index) to use for storing or retrieving reservation details.
2. Each pigeonhole corresponds to a specific date and room number (key).
3. If two reservations map to the same pigeonhole (collision), the receptionist uses a list to keep both reservations (chaining).

---

## Hash Tables in Programming

Hash tables are implemented in various programming languages under different names:
- **Python**: `dict`
- **Java**: `HashMap`
- **C++**: `unordered_map`
- **JavaScript**: `Object` or `Map`

### Example in Python:
```python
# Creating a hash table
hash_table = {}

# Adding key-value pairs
hash_table["Room 101: 20/09/2023"] = "Alice"
hash_table["Room 102: 20/09/2023"] = "Bob"

# Accessing values
print(hash_table["Room 101: 20/09/2023"])  # Output: Alice

# Checking for a key
print("Room 103: 21/09/2023" in hash_table)  # Output: False

# Removing a key-value pair
del hash_table["Room 101: 20/09/2023"]
