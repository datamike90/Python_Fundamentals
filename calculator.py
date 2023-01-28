
def calculadora():
    while True:
        num1 = float(input("Ingresa el primer número: "))
        operacion = input("Ingresa la operación a realizar (+, -, *, /): ")
        num2 = float(input("Ingresa el segundo número: "))

        if operacion == "+":
            resultado = num1 + num2
        elif operacion == "-":
            resultado = num1 - num2
        elif operacion == "*":
            resultado = num1 * num2
        elif operacion == "/":
            resultado = num1 / num2
        else:
            print("Operación no válida")
            continue
        print("El resultado es: ", resultado)
        continuar = input("Desea realizar otra operación (s/n)?: ").lower()
        if continuar == "n":
            break

calculadora()
