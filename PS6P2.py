#input

StartValue = int(input("Enter a start value: "))
StopValue = int(input("Enter a stop value: "))
IncrementValue = int(input("Enter an increment value: "))

#processing and output

while StartValue <= StopValue:
    print(StartValue)
    StartValue = StartValue + IncrementValue