#input

TicketQty = float(input("Enter number of concert tickets."))

#process

if TicketQty >= 25:
  TicketPrice = 50
else:
  if TicketQty >= 10:
    TicketPrice = 60
  else:
    if TicketQty >= 5:
      TicketPrice = 70
    else:
      TicketPrice = 75

TotalCost = TicketQty * TicketPrice

#output

print("The number of tickets is ", TicketQty, " and the price per ticket is $", TicketPrice, ". The total cost is $", TotalCost, ".")