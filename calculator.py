#Simple Calculator

print("Welcome to Calculator")
print("--------- Menu --------")
print("Press + for ADDITION")
print("Press - for SUBSTRACTION")
print("Press * for MULTIPLICATION")
print("Press / for DIVISION")
print("-----------------------")

firstNum = int(input("Enter first Number :"))
secondNum = int(input("Enter second Number :"))
ch = input("Please enter your CHOICE :")

if ch == "+":


    print("Anwser :"+str(firstNum+secondNum))

elif ch == "-":
    print("Anwser :"+str(firstNum - secondNum))

elif ch == "*":
    print("Anwser :"+str(firstNum * secondNum))

elif ch == "/":
    print("Anwser :"+str(firstNum / secondNum))
