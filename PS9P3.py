def CompMPG(Miles, Gallons):
  MPG = Miles/Gallons
  return MPG

Trips = 0
Prompt = input("Do you want to calculate MPG?")

while Prompt == "y" or Prompt == "Y" or Prompt == "Yes" or Prompt == "YES"or Prompt == "yes":
  DestCity = input("Enter the destination city: ")
  Miles = int(input("Enter the miles traveled: "))
  Gallons = int(input("Enter the gallons used: "))
  MPG = CompMPG(Miles, Gallons)
  print("You travelled ", Miles, " miles to ", DestCity)
  print("Miles per gallon: ", MPG)
  Trips = Trips + 1
  Prompt = input("Do you want to calculate MPG?")

print("You calculated the MPG for", Trips, "trip(s)!")