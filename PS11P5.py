Total = 0.0
Tax = 0.0
def ComputeTotal (Qty, Price):
  global Total
  Total = Qty * Price
  global Tax
  Tax = Total * .07
  return

Qty = float(input("Enter quantity of item: "))
Price = float(input("Enter price per unit: "))
ComputeTotal(Qty, Price)
print("Total: ", format(float(Total), '10,.2f'))
print("Tax: ", format(float(Tax), '10,.2f'))