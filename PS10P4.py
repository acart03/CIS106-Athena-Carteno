def CompTickPrice(MFDTC):
  if MFDTC >= 30:
    TicketPrice = 12.00
  elif MFDTC >= 20 and MFDTC <=29:
    TicketPrice = 10.00
  elif MFDTC >= 10 and MFDTC <=19:
    TicketPrice = 8.00
  else:
    TicketPrice = 5.00
  return TicketPrice


Prompt = input("Do you want to calculate ticket price?")
TotalPrice = 0.0
TicketPrice = 0.0

while Prompt == "Yes" or Prompt == "yes" or Prompt == "YES" or Prompt == "Y" or Prompt == "y":
  MFDTC = int(input("Enter distance from downtown Chicago: "))
  TicketPrice = CompTickPrice(MFDTC)
  print("The ticket price is: $", TicketPrice)
  Prompt = input("Do you want to calculate ticket price?")
  TotalPrice = TotalPrice + TicketPrice
print ("The total for all calculated tickets is: $", TotalPrice)