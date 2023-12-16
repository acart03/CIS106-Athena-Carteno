def CompAsVal(County, MarkVal):
  if County == "Cook":
    AsVal = MarkVal * .9
  elif County == "DuPage":
    AsVal =MarkValmv * .8
  elif County == "McHenry":
    AsVal = MarkVal * .75
  elif County == "Kane":
    AsVal = MarkVal * .6
  else:
    AsVal = MarkVal * .7
  return AsVal


Prompt = input("Do you want to calculate the assessed value of a home?")
Total = 0.0

while Prompt == "Yes" or Prompt == "yes" or Prompt == "YES" or Prompt == "Y" or Prompt == "y":
  County = input("What is the county? ")
  MarkVal = float(input("What is the home's market value?: $"))
  AsVal = CompAsVal(County, MarkVal)
  print("The assessed value of the home is: $", AsVal)
  Prompt = input("Do you want to calculate the assessed value of a home?")
  Total = Total + AsVal
print("The final assessed value of the homes is: $", Total)