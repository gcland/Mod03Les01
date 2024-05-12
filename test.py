service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}

print(service_tickets)
ticketnum = "Ticket001"
cust_name = input("customer name?")
service_tickets[ticketnum]["Customer"] = cust_name

print(service_tickets)