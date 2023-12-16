class Student:
  def __init__(self, FirstName, LastName,
               DistCode, EnCredits):
    self.FirstName = FirstName
    self.LastName = LastName
    self.districtcode = DistCode
    self.enrolledcredits = EnCredits

  def tuitionowed(self, DistCode, EnCredits):
    if DistCode == "I":
     Total = EnCredits * 250.00
    else:
      Total = EnCredits * 500.00
    return Total

  def fullname(self):
    return "{} {}".format(self.FirstName, self.LastName)

StudentOne = Student("John", "Doe", "I", 9)
StudentTwo = Student("Jane", "Doe", "O", 9)

StudentOne.fullname()
print(Student.fullname(StudentOne))
print("Enrolled credits: ", StudentOne.enrolledcredits)
print("District code: ", StudentOne.districtcode)
print("Tuition owed: $", StudentOne.tuitionowed(StudentOne.districtcode, StudentOne.enrolledcredits))
print(" ")
StudentTwo.fullname()
print(Student.fullname(StudentTwo))
print("Enrolled credits: ", StudentTwo.enrolledcredits)
print("District code: ", StudentTwo.districtcode)
print("Tuition owed: $", StudentTwo.tuitionowed(StudentTwo.districtcode, StudentTwo.enrolledcredits))