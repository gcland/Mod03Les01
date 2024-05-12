service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "open"}
}

def ticket_status_filter(): #filters by closed or open status tickets
    while True:
        choice = input("Filter tickets by open/closed? (yes/no) ")
        if choice.lower() == "yes":
            close_open = input("Would you like to see open or closed tickets? ")
            if close_open.lower() == "closed":
                for ticketnum, customer in service_tickets.items():
                    if service_tickets[ticketnum]["Status"].lower() == "closed":
                        print()
                        print(ticketnum + ":")
                        for issue in customer:
                            print(issue + ":", customer[issue])
                            break
            elif close_open.lower() == "open":
                for ticketnum, customer in service_tickets.items():        
                    if service_tickets[ticketnum]["Status"].lower() == "open":
                        print()
                        print(ticketnum + ":")
                        for issue in customer:
                            print(issue + ":", customer[issue])
                            break
            else:
                print("Command not recognized. Please try again.")
        else:
            break
        
def all_status(): #displays all tickets
    for ticketnum, customer in service_tickets.items():
        print()
        print(ticketnum + ":")
        for issue in customer:
            print(issue + ":", customer[issue])
    ticket_status_filter()

def open(): #open tickets
    i = 3
    while True:
        cust_name = input("What is the customer's name? ")
        if cust_name.lower() == "end":
            break
        issue_name = input("What is the issue? ")
        if issue_name.lower() == "end":
                break
        ticketnum = "Ticket00"+str(i)
        service_tickets.update({ticketnum: {"Customer": cust_name, "Issue": issue_name, "Status": "open"}})
        i+=1
        print(f"\n{ticketnum} opened!")
        print(f"Customer: " + service_tickets[ticketnum]["Customer"])
        print(f"Issue: " + service_tickets[ticketnum]["Issue"])
        print(f"Status: " + service_tickets[ticketnum]["Status"])
        again = input("Would you like to open another ticket? ")
        if again.lower() == "yes":
            continue
        else:
            break

def update(): #update ticket customer name, issue name, or close ticket
    while True:
        see_tickets = input("See all tickets? (yes/no) ")
        if see_tickets.lower() == "yes":
            all_status()
        ticketnum = ("Ticket"+str(input("Enter ticket ID number: ")))
        print(ticketnum)
        if ticketnum in service_tickets:
            print(service_tickets[ticketnum])
            updateprompt = input("Would you like to update this ticket? ")
            if updateprompt.lower() == "yes":
                valueprompt = input("Update customer name, update issue, or close ticket? ")
                if valueprompt.lower() == "update customer name":
                    cust_name = input("What is the customer's name? ")
                    service_tickets[ticketnum]["Customer"] = cust_name
                    print(service_tickets[ticketnum])
                    break
                elif valueprompt.lower() == "update issue":
                    issue_name = input("What is the issue? ")
                    service_tickets[ticketnum]["Issue"] = issue_name
                    print(service_tickets[ticketnum])
                    break
                elif valueprompt.lower() == "close ticket":
                    service_tickets[ticketnum]["Status"] = "closed"
                    print(service_tickets[ticketnum])
                else:
                 print("Command not recognized. Please try again.")
            else:
                print("Command not recognized. Please try again.")
        else:
            print("This ticket number does not exist!")

def close():
    while True:
        ticketnum = ("Ticket"+str(input("Enter ticket ID number: ")))
        print(ticketnum)
        if ticketnum in service_tickets:
            print(service_tickets[ticketnum])
            updateprompt = input("Would you like to close this ticket? ")
            if updateprompt.lower() == "yes":
                service_tickets[ticketnum]["Status"] = "closed"
                print(service_tickets[ticketnum])
            else:
                print("Command not recognized. Please try again.")
            again = input("Would you like to open another ticket? ")
            if again.lower() == "yes":
                continue
            else:
                break
        else:
            print("This ticket number does not exist!")

while True:
    print()
    display = input("Welcome to ticket tracking software! Which of the following options would you like to do: \n 1. Display all tickets \n 2. Filter by open or closed tickets \n 3. Open a new ticket \n 4. Update properties of a ticket \n 5. Close a ticket \n >> ")
    if str(display) == "1":
        all_status()
    elif str(display) == "2":
        ticket_status_filter()
    elif str(display) == "3":
        open()
    elif str(display) == "4":
        update()
    elif str(display) == "5":
        close()
    elif display.lower() == "end":
        break
    else:
        print("Command not recognized! Please enter a command, 1 - 5 or 'end' to finish.")