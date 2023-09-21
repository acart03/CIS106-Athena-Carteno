#input

Name = input("What is the name of the appliance?")
Cost = float(input("What is the cost of the appliance?"))

#processing

if Cost > 1000:
  Warrantee = .10 * Cost
else:
  Warrantee = .05 * Cost

Total = Warrantee + Cost

#output

print("For the ", Name, ", the cost is $", Cost, ". The warrantee is $", Warrantee, " and the total is $", Total, ".")