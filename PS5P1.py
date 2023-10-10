#input

WidgetQty = float(input("Input the quantity of widgets."))

#processing
#using nested IF statements

if WidgetQty > 10000:
  Price = 10
else:
  if WidgetQty > 5000:
    Price = 20
  else:
    Price = 30

ExtPrice = WidgetQty * Price
TaxAmount = ExtPrice * 0.07
Total = TaxAmount + ExtPrice

#output

print("The extended price is $", ExtPrice, ". The tax amount is $", TaxAmount, ". The total is $", Total, ".")