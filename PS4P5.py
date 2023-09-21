#input

LastName = input("Please enter your last name.")
DependentQty = int(input("What is the number of dependents?"))
GrossIncome = float(input("Enter the gross income."))

#processing

AdjGross = GrossIncome - (DependentQty * 12000)

if AdjGross > 50000:
  TaxRate = .20
else:
  TaxRate = .10

IncomeTax = AdjGross * TaxRate

if IncomeTax < 0:
  IncomeTax = 100
else:
  IncomeTax = IncomeTax

#output

print("Mister/Miss", LastName, ", your gross income is $", GrossIncome, " for ", DependentQty, "dependents. The adjusted gross income is $", AdjGross, " and the income tax is $", IncomeTax, "."  )