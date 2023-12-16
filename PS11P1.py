def discount(Qty, Price, DiscRate):
  Total = Qty * Price
  DiscAmt = DiscRate * Total
  DiscPrice = Total - DiscAmt

  return DiscAmt, DiscPrice

Qty = float(input("Enter the quantity: "))
Price = float(input("Enter the unit price: $"))
DiscRate = float(input("Enter the discount rate (%): "))
DiscAmt, DiscPrice = discount(Qty, Price, DiscRate)

print("There was a quantity of", Qty, "units at $", Price, "each.")
print("Discounted amount: $", DiscAmt)
print("Discounted price: $", DiscPrice)