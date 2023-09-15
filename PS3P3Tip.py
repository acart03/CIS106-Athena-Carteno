#input phase

MealTotal = float(input("Please input the meal total."))

#Processing phase

FifteenTip = MealTotal * .15
EighteenTip = MealTotal * .18
TwentyTip = MealTotal * .20

FifteenTotal = MealTotal + FifteenTip
EighteenTotal = MealTotal + EighteenTip
TwentyTotal = MealTotal + TwentyTip

#Output phase

print("With 15% Tip:", "\n Total: $", MealTotal, "\n Tip: $", FifteenTip, "\n Total with Tip: $", FifteenTotal)

print(" ")

print("With 18% Tip:", "\n Total: $", MealTotal, "\n Tip: $", EighteenTip, "\n Total with Tip: $", EighteenTotal)

print(" ")

print("With 20% Tip:", "\n Total: $", MealTotal, "\n Tip: $", TwentyTotal, "\n Total with Tip: $", TwentyTotal)
