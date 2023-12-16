p = open("p3.txt", "r")

#initialize sums to 0
TotalBonus = 0.0

#get first data line
LastName = str(p.readline().rstrip('\n'))

while LastName !="":
  Salary = float(p.readline())

  if Salary >= 100000.00:
    Bonus = Salary * .2
  elif Salary == 50000.00:
    Bonus = Salary * .15
  else:
    Bonus = Salary * .1

  TotalBonus = TotalBonus + Bonus

  print("Employee last name: ", LastName)
  print("Employee salary: $", Salary)
  print(LastName, "'s bonus: $", Bonus)
  print("")


  LastName = str(p.readline().rstrip('\n'))

p.close()

print("Total bonus paid out: $", TotalBonus)