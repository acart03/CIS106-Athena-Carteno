def BowlAvg(ScoreOne, ScoreTwo, ScoreThree, Handicap):
  Sum = ScoreOne + ScoreTwo + ScoreThree
  Avg = Sum / 3
  HAvg = (Sum + Handicap) / 3
  return Avg, HAvg

LastName = input("Enter bowler's last name: ")
ScoreOne = float(input("Enter first score: "))
ScoreTwo = float(input("Enter second score: "))
ScoreThree = float(input("Enter third score: "))
Handicap = float(input("Enter handicap: "))
Avg, HAvg = BowlAvg(ScoreOne, ScoreTwo, ScoreThree, Handicap)
print("Bowler: ", LastName)
print("Average: ", format(float(Avg), '10,.2f'))
print("Handicap: ", format(float(HAvg), '10,.2f'))