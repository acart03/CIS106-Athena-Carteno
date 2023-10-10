#input

LastName = input("Enter your last name.")
Salary = float(input("Enter your salary."))
JobLevel = float(input("Enter your job level."))

#processing

if JobLevel >= 10:
  BonusRate = 0.25
else:
  if JobLevel >= 5:
    BonusRate = 0.20
  else: 
    BonusRate = 0.10

Bonus = Salary * BonusRate

#output

print("Mister/Miss", LastName, ", your bonus is $", Bonus, ".")