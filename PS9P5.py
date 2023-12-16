def CompOwed(Credit, DistrictCode, Cost):

  if DistrictCode == "I":
    Cost = 250.00
  else:
    Cost = 550.00

  Owed = Credit * Cost

  return Owed

Tuition = 0.0
Prompt = input("Do you want to calculate tuition owed?: ")

while Prompt == "y" or Prompt == "Y" or Prompt == "yes" or Prompt == "YES" or Prompt == "Yes":
  LastName = input("Enter student's last name: ")
  Credit = int(input("Enter number of credit hours: "))
  DistrictCode = input("Enter student's district code: ")
  Cost = 0.0
  Owed = CompOwed(Credit, DistrictCode, Cost)
  print(LastName, " tuition owed: $", Owed)
  Tuition = Tuition + Owed

  Prompt = input("Do you want to calculate tuition owed?: ")

print("Total tuition owed: $", Tuition) 