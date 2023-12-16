p = open("p4.txt", "r")

count = 0.0
TotalExtPrice = 0.0


Item = str(p.readline().rstrip('\n'))

while Item !="":
  Qty = float(p.readline())
  Price = float(p.readline())

  ExtPrice = Qty * Price
  TotalExtPrice = TotalExtPrice + ExtPrice
  count = count + 1


  print("Item is:           ", Item)
  print("Quantity is:       ", Qty)
  print("Price is:          ", Price)
  print("Extended price is: ", ExtPrice)

  Item = str(p.readline().rstrip('\n'))


print("Total extended prices: ", TotalExtPrice)
print("Number of orders:      ", count)
Avg = TotalExtPrice/count
print("Average order:         ", Avg)