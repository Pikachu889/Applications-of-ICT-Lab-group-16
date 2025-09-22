while True:
    num1 = int(input("Enter the first number : "))
    num2 = int(input("Enter the second number : "))
    op = input("Enter +, -, *, / , // , % , ** etc for the specific operation : ")
    if op == "+":
        result = num1 + num2
    elif op == "-":
         result = num1 - num2
    elif op == "*":
         result = num1 * num2
    elif op == "/":
        result = num1 / num2
    elif op == "//":
        result = num1 // num2
    elif op == "%":
        result = num1 % num2
    elif op == "**":
        result = num1 ** num2
    else:
        print("Invalid operation entered!")
        continue
    print("The result of given numbers is : " , result)
    cnt = input("Do You wish to continue another operation? (Yes/No) : ")
    if cnt != "Yes":
        print("Thanks for using the program, it will now exit!")
        break
    else:
        continue