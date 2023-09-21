#input

ItemQty = float(input("Enter the item quantity."))

#processing

if ItemQty >= 1000:
  UnitPrice = 3.00
else:
  UnitPrice = 5.00

ExtPrice = ItemQty * UnitPrice
Tax = ExtPrice * 0.07
Total = ExtPrice + Tax

#output
#spacing the output print as a personal preference 

print(" ")
print("The item quantity is", ItemQty, ".")
print(" ")
print("The unit price is $", UnitPrice, ".")
print(" ")
print("The extended price is $", ExtPrice, ".")
print(" ")
print("The tax is $", Tax, ".")
print(" ")
print("The total is $", Total, ".")