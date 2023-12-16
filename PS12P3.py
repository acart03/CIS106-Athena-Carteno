def displaynames(LastName, score):
  for i in LastName, score:
    print(i)

  l = len(LastName)
  print("Lastname and respective score")
  for x in range(0,l,1):
    print(x, " " , LastName[x], "received a score of: " , score[x])

def HighLow(LastName, score):
  l = len(LastName)
  HighScore = -1.0
  LowScore = 99999999.99
  for y in range (0,l,1):
    if float(score[y]) > float(HighScore):
      HighIndex = y
      HighScore = score[y]

    if float(score[y]) < float(LowScore):
      LowIndex = y
      LowScore = score[y]

  print("Highest score:", LastName[HighIndex], score[HighIndex])
  print("Lowest score:", LastName[LowIndex], score[LowIndex]) 

f = open("p3.txt", "r")

# arrays
LastName = []
score = []

LNames = f.readline()

while LNames != "":
  LastName.append(str(LNames).rstrip("\n"))
  s = float(f.readline())
  score.append(s)
  LNames = f.readline()
f.close()
displaynames(LastName, score)
HighLow(LastName, score)