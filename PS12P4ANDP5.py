def displaynames(LastName, BatAvg):
  l = len(LastName)
  print("Lastname and batting average:")
  for x in range(0,l,1):
    print(x, " " , LastName[x], "batting average: " , BatAvg[x])

def seqsearch(LastName, sname):
  l = len(LastName)
  i = -1
  for y in range(0,l,1):
   if LastName[y] == sname:
     i = y

  return i


f = open("p4.txt", "r")

# arrays
LastName = []
BatAvg = []

LastName = f.readline()

while LastName != "":
  LastName.append(str(LastName).rstrip("\n"))
  s = float(f.readline())
  BatAvg.append(s)
  LastName = f.readline()
f.close()
displaynames(LastName, BatAvg)

Prompt = input("Do you want to search for a name?")

while Prompt == "Yes" or Prompt == "YES" or Prompt == "yes" or Prompt == "y" or Prompt == "Y":
  sname = input("Enter last name to search for: ")
  i = seqsearch(LastName, sname)
  if i == -1:
    print(sname, "not found.")
  else:
    print (LastName[i], " has a batting average of ", BatAvg[i])

  Prompt = input("Do you want to search for another name?")