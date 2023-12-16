counter = 0
GrossSum = 0.0

PromptValue = input("Do you want to compute your gross pay?")

while PromptValue == "Yes" or PromptValue == "y" or PromptValue == "Y" or PromptValue == "YES" or PromptValue == "yes":
  counter = counter + 1
  LastName = input("Enter last name: ")
  TotalHours = int(input("Enter hours worked: "))
  PayRate = float(input("Enter hourly rate: "))
  if TotalHours >= 40:
    GrossPay = (40 * PayRate) + ((TotalHours - 40) * (PayRate * 1.5))
  else:
    GrossPay = PayRate * TotalHours
  print("Mister/Miss ", LastName, ", your gross pay is: $", GrossPay)
  GrossSum = GrossSum + GrossPay
  PromptValue = input("Do you want to compute your gross pay?")

print("Sum of pay roll: $", GrossSum)
print("Number of employees: ", counter)
AvgGrossPay = GrossSum / counter
print("Average gross pay is: $", AvgGrossPay)