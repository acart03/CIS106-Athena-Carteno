PromptValue = input("Do you want to compute the annual interest?")

InterestAcc = 0.0  

while PromptValue == "Yes" or PromptValue == "yes" or PromptValue == "YES" or PromptValue == "Y" or PromptValue == "y":
  BeginBalance = float(input("Enter principle: "))
  Rate = float(input("Enter interest rate: "))
  InterestAcc = 0.0  
  for count in range (1,6, ):
    Annual = BeginBalance * Rate
    EndBalance = BeginBalance + Annual
    print(count, "  ", BeginBalance, "  ", EndBalance)
    BeginBalance = EndBalance
    InterestAcc = InterestAcc + Annual

  PromptValue = input("Do you want to compute the annual interest?")
print("Total interest earned", InterestAcc)