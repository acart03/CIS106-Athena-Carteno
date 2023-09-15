#input phase

FirstName = input("Please enter your first name.")
StepCount = float(input("Please enter the number of steps you walked in a day."))

#processing phase

Calories = StepCount * .25

#output phase

print(FirstName, ", you burned ", Calories, " calories.")