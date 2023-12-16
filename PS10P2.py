SquareF = 0.0
def CompSquareF(length, width, height):
  SquareF = (2 * (length * width) + 2 * (length * height) + 2 * (width * height))
  return SquareF

def CompNumGal(Total):
  NumGal = Total/50
  return NumGal

Total = 0.0
Prompt = input("Do you want to calculate square footage?")

while Prompt == "Yes" or Prompt == "yes" or Prompt == "YES" or Prompt == "y" or Prompt == "Y":
  length = int(input("Enter the length of the room: "))
  width = int(input("Enter the width of the room: "))
  height = int(input("Enter the height of the room: "))
  SquareF = CompSquareF(length, width, height)
  print("The square footage of the room is", SquareF)
  Total = Total + SquareF
  Prompt = input("Do you want to calculate square footage?")

NumGal = CompNumGal(Total)
print("The number of gallons needed ", NumGal)