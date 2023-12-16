def displayarrays(LastNames):
  for i in range(0, 10, 1):
    print(LastNames[i])

def rdisplay(LastNames):
  for i in range (9, -1, -1):
    print(LastNames[i])

LastNames = ["Anderson", "Bennet", "Carter", "Donovan", "Evans", "Franklin", "Gallagher", "Hamilton", "Ingram", "Jennings"]

print("List of names: ")
displayarrays(LastNames)
print("List of names in reverse order: ")
rdisplay(LastNames)