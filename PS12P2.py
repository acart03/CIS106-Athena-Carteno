def displayarrays(LastNames, ExamScore):
  for i in range(0, 10, 1):
    print(LastNames[i], "received an exam score of ", ExamScore[i])


LastNames = ["Anderson", "Bennet", "Carter", "Donovan", "Evans", "Franklin", "Gallagher", "Hamilton", "Ingram", "Jennings"]
ExamScore = [95.5, 89.1, 59.2, 100.0, 84.5, 76.5, 79.2, 79.3, 78.9, 99.9]
print("List of names with respective score: ")
displayarrays(LastNames, ExamScore)