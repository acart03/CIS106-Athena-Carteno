#input

QtyBooks = int(input("Please enter the number of books."))
BookCost = float(input("Please enter the cost per book."))

#processing

Total = QtyBooks * BookCost
if Total > 50:
  Shipping = 0
else:
  Shipping = 25

#output

print("The order total is $", Total, ". The shipping total is $", Shipping, ".")