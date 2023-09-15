#input phase

FixedCosts = float(input("Please enter the fixed cost."))
UnitPrice = float(input("Please enter the price per unit."))
UnitCost = float(input("Please enter the cost per unit."))

#processing phase

BreakEven = FixedCosts / (UnitPrice - UnitCost)

#output phase

print("The break even point for your business is $", BreakEven, ".")