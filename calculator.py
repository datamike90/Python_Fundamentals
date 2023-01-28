def calculator():
    while True:
        num1 = float(input("Enter the first number: "))
        operacion = input("Enter the operation to make (+, -, *, /): ")
        num2 = float(input("Enter the second number: "))

        if operacion == "+":
            resultado = num1 + num2
        elif operacion == "-":
            resultado = num1 - num2
        elif operacion == "*":
            resultado = num1 * num2
        elif operacion == "/":
            resultado = num1 / num2
        else:
            print("Operation is not valid")
            continue
        print("The result is: ", resultado)
        continuar = input("Do you want to carry out another operation (s/n)?: ").lower()
        if continuar == "n":
            break

calculator()
