p = open("p5.txt", "r")

TotalTuition = 0.0
count = 0

LastName = str(p.readline().rstrip('\n'))

while LastName != "":
  DistCode = str(p.readline().rstrip('\n'))
  Credits = float(p.readline())

  if DistCode == "I":
    Cost = 250.00
  else:
    Cost = 500.00

  Tuition = Credits * Cost
  count = count + 1
  TotalTuition = TotalTuition + Tuition

  print("Student: ",LastName)
  print("Credits taken: " , Credits)
  print("Tuition owed: ", Tuition)
  print(" ")

  LastName = str(p.readline().rstrip('\n'))

p.close()

print("Total tuition owed: ", TotalTuition)
print("Number of students: ", count)