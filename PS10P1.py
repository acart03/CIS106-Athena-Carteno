Percent = 0.0

def ComputeNext(Month, Sales):
    global Percent  # Define Percent as global
    if Month == "Jan" or Month == "Feb" or Month == "Mar":
        Percent = 0.1
    elif Month == "Apr" or Month == "May" or Month == "Jun":
        Percent = 0.15
    elif Month == "Jul" or Month == "Aug" or Month == "Sep":
        Percent = 0.2
    elif Month == "Oct" or Month == "Nov" or Month == "Dec":
        Percent = 0.25
    else:
        print("Re-enter forecasting period in 'Mmm' format")

    NextMonFore = Sales * (1 + Percent)
    return NextMonFore

Prompt = input("Do you want to compute next month's forecast?")

while Prompt.lower() in ["yes", "y"]:
    LastName = input("Enter last name: ")
    Month = input("Enter forecasting month: ")
    Sales = float(input("Enter sales: "))
    NextMonFore = ComputeNext(Month, Sales)
    print(LastName, "calculated a monthly forecast of $", NextMonFore, "for the month of ", Month)
    Prompt = input("Do you want to compute next month's forecast?")

print(LastName, "calculated a monthly forecast of $", NextMonFore, "for the month of ", Month)