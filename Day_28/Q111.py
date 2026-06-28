class Event:
    def __init__(self, event_id, name, total_seats, price):
        self.event_id = event_id
        self.name = name
        self.total_seats = total_seats
        self.available_seats = total_seats
        self.price = price


class Booking:
    def __init__(self, booking_id, event_id, customer_name, seats):
        self.booking_id = booking_id
        self.event_id = event_id
        self.customer_name = customer_name
        self.seats = seats


class TicketSystem:
    def __init__(self):
        self.events = {}
        self.bookings = {}
        self.next_event_id = 1
        self.next_booking_id = 1

    def add_event(self, name, total_seats, price):
        event = Event(self.next_event_id, name, total_seats, price)
        self.events[self.next_event_id] = event
        self.next_event_id += 1
        return event.event_id

    def remove_event(self, event_id):
        if event_id in self.events:
            del self.events[event_id]
            return True
        return False

    def book_ticket(self, event_id, customer_name, seats):
        if event_id not in self.events:
            return None
        event = self.events[event_id]
        if seats > event.available_seats:
            return None
        event.available_seats -= seats
        booking = Booking(self.next_booking_id, event_id, customer_name, seats)
        self.bookings[self.next_booking_id] = booking
        self.next_booking_id += 1
        return booking.booking_id

    def cancel_booking(self, booking_id):
        if booking_id not in self.bookings:
            return False
        booking = self.bookings[booking_id]
        event = self.events.get(booking.event_id)
        if event:
            event.available_seats += booking.seats
        del self.bookings[booking_id]
        return True

    def get_total_cost(self, booking_id):
        if booking_id not in self.bookings:
            return None
        booking = self.bookings[booking_id]
        event = self.events.get(booking.event_id)
        if not event:
            return None
        return booking.seats * event.price

    def list_events(self):
        return list(self.events.values())

    def list_bookings(self):
        return list(self.bookings.values())


def display_event(event):
    print(f"ID: {event.event_id} | Name: {event.name} | Available: {event.available_seats}/{event.total_seats} | Price: {event.price}")


def display_booking(booking):
    print(f"Booking ID: {booking.booking_id} | Event ID: {booking.event_id} | Customer: {booking.customer_name} | Seats: {booking.seats}")


def main():
    system = TicketSystem()
    while True:
        print("\n1. Add Event\n2. Remove Event\n3. Book Ticket\n4. Cancel Booking"
              "\n5. View Total Cost\n6. List Events\n7. List Bookings\n8. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Event name: ")
            seats = int(input("Total seats: "))
            price = float(input("Price per seat: "))
            event_id = system.add_event(name, seats, price)
            print(f"Event added with ID {event_id}")

        elif choice == "2":
            event_id = int(input("Event ID: "))
            if system.remove_event(event_id):
                print("Event removed")
            else:
                print("Event not found")

        elif choice == "3":
            event_id = int(input("Event ID: "))
            name = input("Customer name: ")
            seats = int(input("Number of seats: "))
            booking_id = system.book_ticket(event_id, name, seats)
            if booking_id:
                print(f"Booking successful, ID: {booking_id}")
            else:
                print("Booking failed")

        elif choice == "4":
            booking_id = int(input("Booking ID: "))
            if system.cancel_booking(booking_id):
                print("Booking cancelled")
            else:
                print("Booking not found")

        elif choice == "5":
            booking_id = int(input("Booking ID: "))
            cost = system.get_total_cost(booking_id)
            if cost is not None:
                print(f"Total cost: {cost}")
            else:
                print("Booking not found")

        elif choice == "6":
            for e in system.list_events():
                display_event(e)

        elif choice == "7":
            for b in system.list_bookings():
                display_booking(b)

        elif choice == "8":
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()