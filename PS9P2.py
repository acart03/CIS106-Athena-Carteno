def ComputeBatAvg(Hits, Bats):
  BatAvg = Hits/Bats
  return BatAvg

c = 0
prompt = input("Do you want to calculate batting average?")

while prompt == "y" or prompt == "Y" or prompt == "Yes" or prompt == "yes" or prompt == "YES":
  LastName = input("Enter player's last name: ")
  Hits = int(input("Enter the number of hits: "))
  Bats = int(input("Enter the number of at bats: "))
  BatAvg = ComputeBatAvg(Hits, Bats)
  print(LastName, "'s batting average is: ", BatAvg)
  c = c + 1
  prompt = input("Do you want to calculate batting average?")

print("You calculated batting average for ", c, " players!")