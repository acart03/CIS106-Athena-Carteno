#input phase

PriceShare = float(input("Please input the purchase price per share."))
StockPrice = float(input("Please input the current stock price."))
QuantityStock = float(input("Please input the quantity of stock."))

#processing phase

StockValue = (StockPrice - PriceShare)/ QuantityStock

#output phase
#using a boolean to let user know if they are making or losing money.

if StockValue > 0:
  print("The current stock value is $", StockValue, ". You are gaining money.")
else:
  print("The current stock value is $", StockValue, ". You are losing money.")