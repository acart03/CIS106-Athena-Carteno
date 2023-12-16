def SalesRep(Sales):
  if Sales > 100000:
    Comm = Sales * .10
  elif Sales <= 100000:
    Comm = Sales * .05
  Target = Sales * .05
  return Comm, Target

LastName = input("Enter salesperson's last name: ")
Sales = float(input("Enter sales amount: "))
Comm, Target = SalesRep(Sales)
print(LastName, "'s commission earned: $", Comm)
print("Next year's target: $", Target)