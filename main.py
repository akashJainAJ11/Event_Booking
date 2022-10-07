import re

import string


def main():
    eventName = "Python Event"
    eventTickets = 100
    remainingTickets = 100
    bookings = []

    print(remainingTickets)

    print(f"Welcome to our {eventName} booking Application.")
    print(
        f"We have total of {eventTickets} tickets and {remainingTickets} are still available.")
    print("Get your tickets here to attend.")

    while remainingTickets > 0 & len(bookings) < 100:

        # ask user input

        userFirstName = input("Please enter your first name: ")
        userLastName = input("Please enter your last name: ")
        userEmail = input("Please enter your email address: ")
        userTickets = int(input("Enter number of tickets: "))

        isValidName = len(userFirstName) >= 2 and len(userLastName) >= 2
        isValidEmail = re.search("@", userEmail)
        isValidTicketNumber = userTickets > 0 and userTickets <= remainingTickets

        if isValidTicketNumber and isValidName and isValidEmail:
            remainingTickets = remainingTickets - userTickets
            print(
                f"Thank You  {userFirstName} {userLastName} for booking {userTickets}  tickets. You will receive a confirmation email at {userEmail}.")

            print(f"{remainingTickets} tickets are remaining for {eventName}")

            bookings.append(userFirstName)
            print(f"These are all our booking: {bookings}")

        if remainingTickets <= 0:
            # end the program
            print("Our Event is booked out. Come next time.")
            break
        else:
            if not isValidName:
                print("first name and last name you enter is too short")
            if not isValidEmail:
                print("Email address you enter not conatain @ sign")
            if not isValidTicketNumber:
                print("Ticket number you enter is Invalid")
            continue


main()
