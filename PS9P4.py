def CompGrossPay(Hours, JCode, Rate):

  if JCode == "L":
    Rate = 25
  elif JCode == "A":
    Rate = 30
  elif JCode == "J":
    Rate = 50

  if Hours> 40:
    GrossPay = (40 * Rate ) + ((Hours - 40) * Rate * 1.5)
  else:
    GrossPay = Hours * Rate

  return GrossPay

TotalGP = 0
Prompt = input("Do you want to compute gross pay?")

while Prompt == "y" or Prompt == "Y" or Prompt == "yes" or Prompt == "YES" or Prompt == "Yes":
  Rate = float()
  LastName = input("Enter Last Name: ")
  Hours = int(input("Enter hours worked: "))
  JCode = input("Enter job code: ")
  
  if JCode == "L":
    Rate = 25
  elif JCode == "A":
    Rate = 30
  elif JCode == "J":
    Rate = 50
  
  GrossPay = CompGrossPay(Hours, JCode, Rate)
  print("Employee: ", LastName)
  print("Gross pay: ", GrossPay)
  TotalGP = TotalGP + GrossPay

  Prompt = input("Do you want to compute gross pay?")

print("You calculated a total gross pay amount of $", TotalGP)