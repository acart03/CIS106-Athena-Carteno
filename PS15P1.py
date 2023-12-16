class Employee:
  def __init__(self, FirstName, LastName, Pay):
    self.FirstName = FirstName
    self.LastName = LastName
    self.Pay = Pay
    self.email = FirstName + "." + LastName + "@company.com"

  def br(self, rate):
    b = float(rate) * float(self.Pay)
    return b

  def fullname(self):
    return "{} {}".format(self.FirstName, self.LastName)


class Manager(Employee):
  def __init__(self, FirstName, LastName, Pay):
    self.FirstName = FirstName
    self.LastName = LastName
    self.Pay = Pay
    self.email = FirstName + "." + LastName + "@company.com"

  def ltb(self, rate):
      l = float(rate) * float(self.Pay)
      return l


EmpOne = Employee('Athena', 'Carteno', 50000)
EmpTwo = Employee('Test', 'User', 60000)
MngrOne = Manager('Paul', 'Myles', 90000)

#emp_1.fullname()
#print(Employee.fullname(emp_1))
print("Employee: ", EmpOne.fullname())
print("Email: ", EmpOne.email)
print("Pay: $", EmpOne.Pay)
print("10% bonus: ", EmpOne.br(.10))
print("20% bonus: ", EmpOne.br(.20))
print("")
print("Manager: ", MngrOne.fullname())
print("Email: ", MngrOne.email)
print("Pay: $", MngrOne.Pay)
print("Manager 40% bonus: ", MngrOne.ltb(.40))