# Flight Reservation System
# Data Structures: List and Dictionary
# Algorithms: Linear Search and Bubble Sort

flights = [
    {"number": 101, "name": "Air India", "destination": "Delhi",
     "fare": 4500, "seats": 5},

    {"number": 102, "name": "IndiGo", "destination": "Mumbai",
     "fare": 2500, "seats": 4},

    {"number": 103, "name": "SpiceJet", "destination": "Bangalore",
     "fare": 3500, "seats": 6},

    {"number": 104, "name": "Vistara", "destination": "Goa",
     "fare": 3000, "seats": 3}
]


# -------------------------------------------------
# 1. Display All Flights
# -------------------------------------------------

def display_flights(data):

    print("\n---------- AVAILABLE FLIGHTS ----------")
    print("No.\tAirline\t\tDestination\tFare\tSeats")

    for flight in data:
        print(f"{flight['number']}\t"
              f"{flight['name']}\t\t"
              f"{flight['destination']}\t\t"
              f"₹{flight['fare']}\t"
              f"{flight['seats']}")


# -------------------------------------------------
# 2. Linear Search - Search Flight by Number
# -------------------------------------------------

def search_flight(number):

    for flight in flights:

        if flight["number"] == number:
            return flight

    return None


# -------------------------------------------------
# 3. Search Flight by Destination
# -------------------------------------------------

def search_by_destination(destination):

    found = False

    for flight in flights:

        if flight["destination"].lower() == destination.lower():

            print("\nFlight Found!")
            print("Flight Number :", flight["number"])
            print("Airline       :", flight["name"])
            print("Destination   :", flight["destination"])
            print("Fare          : ₹", flight["fare"])
            print("Seats         :", flight["seats"])

            found = True

    if not found:
        print("No flight found for this destination.")


# -------------------------------------------------
# 4. Bubble Sort - Sort by Fare
# -------------------------------------------------

def sort_by_fare():

    sorted_flights = flights.copy()

    n = len(sorted_flights)

    for i in range(n - 1):

        for j in range(n - i - 1):

            if sorted_flights[j]["fare"] > sorted_flights[j + 1]["fare"]:

                sorted_flights[j], sorted_flights[j + 1] = \
                    sorted_flights[j + 1], sorted_flights[j]

    return sorted_flights


# -------------------------------------------------
# 5. Bubble Sort - Sort by Flight Number
# -------------------------------------------------

def sort_by_number():

    sorted_flights = flights.copy()

    n = len(sorted_flights)

    for i in range(n - 1):

        for j in range(n - i - 1):

            if sorted_flights[j]["number"] > \
                    sorted_flights[j + 1]["number"]:

                sorted_flights[j], sorted_flights[j + 1] = \
                    sorted_flights[j + 1], sorted_flights[j]

    return sorted_flights


# -------------------------------------------------
# 6. Book Ticket
# -------------------------------------------------

def book_ticket():

    try:
        number = int(input("Enter flight number: "))

    except ValueError:
        print("Please enter a valid flight number.")
        return

    flight = search_flight(number)

    if flight is None:

        print("Flight not found.")
        return

    if flight["seats"] > 0:

        passenger = input("Enter passenger name: ")

        flight["seats"] -= 1

        print("\n===== TICKET BOOKED SUCCESSFULLY =====")
        print("Passenger Name :", passenger)
        print("Flight Number   :", flight["number"])
        print("Airline         :", flight["name"])
        print("Destination     :", flight["destination"])
        print("Fare            : ₹", flight["fare"])
        print("Remaining Seats :", flight["seats"])

    else:

        print("Sorry! No seats available.")


# -------------------------------------------------
# 7. Cancel Ticket
# -------------------------------------------------

def cancel_ticket():

    try:
        number = int(input("Enter flight number: "))

    except ValueError:
        print("Please enter a valid flight number.")
        return

    flight = search_flight(number)

    if flight is None:

        print("Flight not found.")
        return

    flight["seats"] += 1

    print("\n===== TICKET CANCELLED SUCCESSFULLY =====")
    print("Flight Number   :", flight["number"])
    print("Airline         :", flight["name"])
    print("Destination     :", flight["destination"])
    print("Available Seats :", flight["seats"])


# -------------------------------------------------
# 8. Display Available Seats
# -------------------------------------------------

def display_available_seats():

    print("\n---------- AVAILABLE SEATS ----------")
    print("Flight No.\tAirline\t\tSeats")

    for flight in flights:

        print(f"{flight['number']}\t\t"
              f"{flight['name']}\t\t"
              f"{flight['seats']}")


# -------------------------------------------------
# MAIN MENU
# -------------------------------------------------

while True:

    print("\n======================================")
    print("       FLIGHT RESERVATION SYSTEM")
    print("======================================")

    print("1. Display All Flights")
    print("2. Search Flight by Number")
    print("3. Search Flight by Destination")
    print("4. Sort Flights by Fare")
    print("5. Sort Flights by Flight Number")
    print("6. Book Ticket")
    print("7. Cancel Ticket")
    print("8. Display Available Seats")
    print("9. Exit")

    try:

        choice = int(input("Enter your choice: "))

    except ValueError:

        print("Please enter a valid choice.")
        continue


    # ---------------------------------------------
    # Choice 1 - Display Flights
    # ---------------------------------------------

    if choice == 1:

        display_flights(flights)


    # ---------------------------------------------
    # Choice 2 - Search by Flight Number
    # ---------------------------------------------

    elif choice == 2:

        try:

            number = int(input("Enter flight number to search: "))

            result = search_flight(number)

            if result:

                print("\n===== FLIGHT FOUND =====")
                print("Flight Number :", result["number"])
                print("Airline       :", result["name"])
                print("Destination   :", result["destination"])
                print("Fare          : ₹", result["fare"])
                print("Seats         :", result["seats"])

            else:

                print("Flight not found.")

        except ValueError:

            print("Please enter a valid flight number.")


    # ---------------------------------------------
    # Choice 3 - Search by Destination
    # ---------------------------------------------

    elif choice == 3:

        destination = input("Enter destination: ")

        search_by_destination(destination)


    # ---------------------------------------------
    # Choice 4 - Sort by Fare
    # ---------------------------------------------

    elif choice == 4:

        sorted_flights = sort_by_fare()

        print("\n===== FLIGHTS SORTED BY FARE =====")

        display_flights(sorted_flights)


    # ---------------------------------------------
    # Choice 5 - Sort by Flight Number
    # ---------------------------------------------

    elif choice == 5:

        sorted_flights = sort_by_number()

        print("\n===== FLIGHTS SORTED BY FLIGHT NUMBER =====")

        display_flights(sorted_flights)


    # ---------------------------------------------
    # Choice 6 - Book Ticket
    # ---------------------------------------------

    elif choice == 6:

        book_ticket()


    # ---------------------------------------------
    # Choice 7 - Cancel Ticket
    # ---------------------------------------------

    elif choice == 7:

        cancel_ticket()


    # ---------------------------------------------
    # Choice 8 - Available Seats
    # ---------------------------------------------

    elif choice == 8:

        display_available_seats()


    # ---------------------------------------------
    # Choice 9 - Exit
    # ---------------------------------------------

    elif choice == 9:

        print("\nThank you for using Flight Reservation System!")
        break


    # ---------------------------------------------
    # Invalid Choice
    # ---------------------------------------------

    else:

        print("Invalid choice. Please try again.")