#input

PrincipleAmt = float(input("Enter a principle amount of a CD."))
YearMaturity = float(input("Enter years to maturity of CD."))

#processing

if PrincipleAmt > 100000 and YearMaturity == 5:
  InterestRate = 0.06
else:
  if PrincipleAmt >= 50000 and YearMaturity == 10:
    InterestRate = 0.05
  else:
    if PrincipleAmt >= 50000 and YearMaturity == 5:
      InterestRate = 0.04
    else:
      InterestRate = 0.02

InterestAmt = PrincipleAmt * InterestRate

#output

print("The principle amount is $", PrincipleAmt, ". The interest rate is ", InterestRate, ". The interest amount is $", InterestAmt, ".")