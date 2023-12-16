def ExamAvg(ExamOne, ExamTwo, ExamThree):
  Sum = ExamOne + ExamTwo + ExamThree
  Avg = (Sum/3)
  Total = ExamOne + ExamTwo + ExamThree
  return Avg, Total

LastName = input("Enter last name: ")
ExamOne = float(input("Enter exam 1 score: "))
ExamTwo = float(input("Enter exam 2 score: "))
ExamThree = float(input("Enter exam 3 score: "))

Avg, Total = ExamAvg(ExamOne, ExamTwo, ExamThree)
print("Last name: ", LastName)
print("Exam score average: ", Avg)
print("Points total: ", Total)