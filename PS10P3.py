Price = 0.0
MSRP = 0.0
def CompOTDP(MSRP, Make, Model):
  if Make == "Honda" and Model == "Accord":
   Price = MSRP - (.1 * MSRP)
  elif Make == "Toyota" and Model == "RAV4":
   Price = MSRP - (.15 * MSRP)
  elif Model == "Electric":
    Price = MSRP - (.3 * MSRP)
  else:
   Price = MSRP - (.05 * MSRP)
  return Price

def CompTotal(Price, MSRP):
  Total = Price + (Price * .07)
  return Total

Prompt = input("Do you want to calculate the car's price?")

while Prompt == "Yes" or Prompt == "y" or Prompt == "Y" or Prompt == "yes" or Prompt == "YES":
  MSRP = float(input("What is the MSRP? "))
  Make = input("What is the make of the car? ")
  Model = input("What is the model of the car? ")
  Price = CompOTDP(MSRP, Make, Model)
  print("The new price is: $", Price)
  Prompt = input("Do you want to calculate the car's price?")

Total = CompTotal(Price, MSRP)
print("The total, final price is: $ ", Total)