

hotel_rooms = {
    "101": {"status": "available", "customer": ""},
    "102": {"status": "booked", "customer": "John Doe"},
    "103": {"status": "available", "customer": ""},
    "104": {"status": "available", "customer": ""},
    "105": {"status": "available", "customer": ""}
}

def all_status():
    for room, status in hotel_rooms.items():
        print()
        print(room + ":")
        for availability in status:
            print(availability + ":", status[availability])

def room_status(x):
    print(x+":")
    print(f"Status: " + hotel_rooms[x]["status"])
    print(f"Customer: " + hotel_rooms[x]["customer"])

def room_check():
    while True:
        room = str(input("Which room # would you like to check the status of? Input, 'end' to finish. "))
        if room in hotel_rooms:
            print(room+":")
            print(f"Status: " + hotel_rooms[room]["status"])
            if hotel_rooms[room]["status"] == "booked":
                print(f"Customer: " + hotel_rooms[room]["customer"])
        elif room.lower() == "end":
            break
        else:
            print("Error, room number does not exist at this hotel! Try again.")
            
def book():
    while True:

        try: 
            x = input("What is the room number? ")
            if hotel_rooms[x]["status"] == "booked":
                print("Room",x, "is already booked.")
                room_status(x)
                
            else:
                cust_name = input("What is the customer's name? ")
                hotel_rooms.update({x: {"status": "available", "customer": cust_name}})
                hotel_rooms.update({x: {"status": "booked", "customer": cust_name}})
                room_status(x)
        except KeyError:
            break

def checkout():
    while True:
        try:
            y = input("What is the room number? ")
            if hotel_rooms[y]["status"] == "available":
                print("Room",y, "is not booked. Please enter a room with a customer.")
            else:
                hotel_rooms.update({y: {"status": "booked", "customer": ""}})
                hotel_rooms.update({y: {"status": "available", "customer": ""}})
                room_status(y)
                break
        except KeyError:
            break

while True:
    display = input("Welcome to hotel software! Which of the following options would you like to do: \n 1. Display the status all rooms \n 2. Check the status of a specific room \n 3. Book a room \n 4. Check out \n >> ")
    if str(display) == "1":
        all_status()
    elif str(display) == "2":
        room_check()
    elif str(display) == "3":
        book()
    elif str(display) == "4":
        checkout()
    elif display.lower() == "end":
        break
    else:
        print("Command not recognized! Please enter a command, 1 - 4 or 'end' to finish.")





