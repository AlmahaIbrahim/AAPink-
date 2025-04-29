# Hotel Booking System

# Class to represent a Room
class Room:
    def __init__(self, roomNumber, roomType, price):
        # Initialize room details
        self.roomNumber = roomNumber
        self.roomType = roomType
        self.price = price

    def displayRoomInfo(self):
        # Display room information
        print(f"Room Number: {self.roomNumber}")
        print(f"Room Type: {self.roomType}")
        print(f"Price per night: {self.price}")

# Class to represent a Guest
class Guest:
    def __init__(self, name, phone):
        # Initialize guest details
        self.name = name
        self.phone = phone

    def displayGuestInfo(self):
        # Display guest information
        print(f"Guest Name: {self.name}")
        print(f"Phone Number: {self.phone}")

# Class to represent a Booking
class Booking:
    def __init__(self, guest, room, checkInDate, checkOutDate):
        # Initialize booking details
        self.guest = guest
        self.room = room
        self.checkInDate = checkInDate
        self.checkOutDate = checkOutDate

    def calculateStayDuration(self):
        # Calculate number of days between check-in and check-out
        try:
            duration = (self.checkOutDate - self.checkInDate).days
            if duration < 0:
                raise ValueError("Check-out date cannot be before check-in date.")
            return duration
        except Exception as e:
            # Handle any error in date calculation
            print(f"Error calculating stay duration: {e}")
            return None

    def displayBookingDetails(self):
        # Display booking information
        print(f"Guest: {self.guest.name}")
        print(f"Room: {self.room.roomNumber}")
        print(f"Check-In Date: {self.checkInDate}")
        print(f"Check-Out Date: {self.checkOutDate}")
        stayDuration = self.calculateStayDuration()
        if stayDuration is not None:
            print(f"Total Nights: {stayDuration}")

# Class to generate Invoice
class Invoice:
    def __init__(self, booking):
        # Initialize invoice with a booking
        self.booking = booking
        self.amount = 0

    def calculateTotal(self):
        # Calculate total amount based on stay duration and room price
        try:
            stayDuration = self.booking.calculateStayDuration()
            if stayDuration is None:
                raise ValueError("Invalid stay duration.")
            self.amount = stayDuration * self.booking.room.price
            if self.amount < 0:
                raise ValueError("Amount cannot be negative.")
            return self.amount
        except Exception as e:
            # Handle any error in total calculation
            print(f"Error calculating invoice amount: {e}")
            return 0

    def displayInvoice(self):
        # Display invoice details
        print("\n--- Invoice ---")
        self.booking.displayBookingDetails()
        totalAmount = self.calculateTotal()
        print(f"Total Amount: {totalAmount}")

# Import datetime to work with dates
import datetime

# Main function to run the booking system
def main():
    # Create a Room
    room1 = Room(101, "Deluxe", 150)

    # Create a Guest
    guest1 = Guest("Alice Smith", "123-456-7890")

    # Set Check-In and Check-Out Dates
    checkIn = datetime.date(2025, 5, 10)
    checkOut = datetime.date(2025, 5, 15)

    # Create a Booking
    booking1 = Booking(guest1, room1, checkIn, checkOut)

    # Generate an Invoice
    invoice1 = Invoice(booking1)

    # Display Information
    room1.displayRoomInfo()
    guest1.displayGuestInfo()
    booking1.displayBookingDetails()
    invoice1.displayInvoice()

# Run the program
if __name__ == "__main__":
    main()
