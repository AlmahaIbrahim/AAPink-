# Room class
class Room:
    def __init__(self, roomNumber, roomType, pricePerNight):
        self.roomNumber = roomNumber
        self.roomType = roomType
        self.pricePerNight = pricePerNight

    def getPrice(self):
        return self.pricePerNight


# Invoice class
class Invoice:
    def __init__(self, invoiceID, nightlyRate, additionalCharges, discountsApplied, totalAmount, paymentMethod):
        self.invoiceID = invoiceID
        self.nightlyRate = nightlyRate
        self.additionalCharges = additionalCharges
        self.discountsApplied = discountsApplied
        self.totalAmount = totalAmount
        self.paymentMethod = paymentMethod

    def calculateTotal(self):
        # Calculate the total amount based on the nightly rate, additional charges, and discounts
        return (self.nightlyRate + self.additionalCharges) - self.discountsApplied


# Customer class
class Customer:
    def __init__(self, customerID, name, email, phoneNumber):
        self.customerID = customerID
        self.name = name
        self.email = email
        self.phoneNumber = phoneNumber


# Create Room objects
room1 = Room(roomNumber="101", roomType="Single", pricePerNight=100)
room2 = Room(roomNumber="102", roomType="Double", pricePerNight=150)

# Create Invoice objects and calculate the total amount
invoice1 = Invoice(invoiceID="I001", nightlyRate=room1.getPrice(), additionalCharges=50, discountsApplied=0,
                   totalAmount=0, paymentMethod="Credit Card")
invoice2 = Invoice(invoiceID="I002", nightlyRate=room2.getPrice(), additionalCharges=100, discountsApplied=10,
                   totalAmount=0, paymentMethod="Cash")

# Calculate the total amount for each invoice
invoice1.totalAmount = invoice1.calculateTotal()
invoice2.totalAmount = invoice2.calculateTotal()

# Create Customer objects
customer1 = Customer(customerID="C001", name="John Doe", email="john.doe@example.com", phoneNumber="123-456-7890")
customer2 = Customer(customerID="C002", name="Jane Smith", email="jane.smith@example.com", phoneNumber="987-654-3210")

# Print the invoice details
print(f"Invoice ID: {invoice1.invoiceID}")
print(f"Customer Name: {customer1.name}")
print(f"Room Number: {room1.roomNumber} ({room1.roomType})")
print(f"Nightly Rate: ${invoice1.nightlyRate}")
print(f"Additional Charges: ${invoice1.additionalCharges}")
print(f"Discounts Applied: ${invoice1.discountsApplied}")
print(f"Total Amount: ${invoice1.totalAmount}")
print(f"Payment Method: {invoice1.paymentMethod}")
print()

print(f"Invoice ID: {invoice2.invoiceID}")
print(f"Customer Name: {customer2.name}")
print(f"Room Number: {room2.roomNumber} ({room2.roomType})")
print(f"Nightly Rate: ${invoice2.nightlyRate}")
print(f"Additional Charges: ${invoice2.additionalCharges}")
print(f"Discounts Applied: ${invoice2.discountsApplied}")
print(f"Total Amount: ${invoice2.totalAmount}")
print(f"Payment Method: {invoice2.paymentMethod}")

