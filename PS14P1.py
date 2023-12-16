class Employee:
  def __init__(self, First, Last, Pay):
    self.first = First
    self.last = Last
    self.pay = Pay
    self.email = First + "." + Last + "@company.com"

  def br(self, Rate):
    b = float(Rate) * float(self.pay)
    return b

  def fullname(self):
    return "{} {}".format(self.first, self.last)

EmpOne = Employee('Athena', 'Carteno', 50000)
EmpTwo = Employee('Test', 'User', 60000)


EmpOne.fullname()
print(Employee.fullname(EmpOne))

print("Email: ", EmpOne.email)
print("Pay: ", EmpOne.pay)
print("10% bonus: ", EmpOne.br(.10))
print("20% bonus: ", EmpOne.br(.20))