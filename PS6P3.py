counter = 0

#input

PromptValue = input("Do you want to compute your average score?")

#processing

while PromptValue == "Yes" or PromptValue == "y" or PromptValue == "Y" or PromptValue == "YES" or PromptValue == "yes":
  counter = counter + 1
  LastName = input("Enter student last name: ")
  ScoreOne = float(input("Enter exam score 1: "))
  ScoreTwo = float(input("Enter exam score 2: "))
  ScoreAverage = (ScoreOne + ScoreTwo)/2
  
  #output
  
  print("Miss/Mister ", LastName, ", your score average was ", ScoreAverage)
  PromptValue = input("Do you want to compute another average score?")

print("Number of students who have executed this program is:", counter)