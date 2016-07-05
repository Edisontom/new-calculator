def calculator_print(operetion):
    if function == "+":
        print(number1 + number2)
    elif function == "-":
        print(number1 - number2)
    elif function == "*":
        print(number1 * number2)
    elif function == "/" and number2 == 0:
        print("Eror")
    elif function == "/":
        print(number1 / number2)
    else:
        print ("Eror")
while True:
    number1 = float(input("Enter first number: "))
    function = str(input("Choise operetion ('+', '-', '*', '/'): "))
    number2 = float(input("Enter second number: "))
    calculator_print(function)
    print()
    exit = str(input("If continue press 'Y' else 'N': "))
    print()
    if exit == 'Y':
        continue
    elif exit == 'N':
        import sys
        sys.exit()