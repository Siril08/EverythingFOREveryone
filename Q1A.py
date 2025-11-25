seats_available = 25

tickets = int(input("Enter the number of seats: "))

if(tickets %2 !=0):
    print("Invalid ticket count")
elif(tickets>seats_available):
    print("Insufficient seat")
else:
    print("Seats Booked")
    updates_seats_available = seats_available - tickets
    print("No of seats available now")
    print(updates_seats_available)