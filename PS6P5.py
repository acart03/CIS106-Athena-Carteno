discountSum = 0
print("Do you want to compute order total?")

promptValue = input()
while promptValue == "Yes" or promptValue == "yes" or promptValue == "y" or promptValue == "Y" or promptValue == "YES":
  print("Input quantity.")
  itemQty = int(input())
  print("Input item price.")
  itemPrice = float(input())
  extendedPrice = itemQty * itemPrice
  if extendedPrice > 10000.0:
    discountAmt = extendedPrice * 0.25
  else:
    discountAmt = extendedPrice * 0.1

  total = extendedPrice - discountAmt
  discountSum = discountSum + discountAmt
  print("Extended price: $" + str(extendedPrice))
  print("Discount amount: $" + str(discountAmt))
  print("Total order amount: $" + str(total))
  print("Do you want to compute order total?")

  promptValue = input()
print("Total discounts: $", discountSum)