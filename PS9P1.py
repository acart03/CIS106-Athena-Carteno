def CompExtPrice(Qty, UnitPrice):
  ExtPrice = Qty * UnitPrice

  if ExtPrice > 10000.00:
    DiscAmt = ExtPrice * (.1)
  else:
    DiscAmt = 0.0

  newEP = ExtPrice - DiscAmt
  return newEP

totalEP = 0.0
Prompt = input("Do you want to compute extended price?")

while Prompt == "y" or Prompt == "Y" or Prompt == "yes" or Prompt == "YES" or Prompt == "Yes":
  Qty = float(input("Enter quantity: "))
  UnitPrice = float(input("Enter unit price: $"))
  newEP = CompExtPrice(Qty, UnitPrice)
  totalEP = totalEP + newEP
  print("Extended price is: $", newEP)
  Prompt = input("Do you want to compute extended price?")

print("Total extended price is: $" , totalEP)