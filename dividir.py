print("Calculadora")

num1 = float(input("Introduce el numerador: "))
num2 = float(input("Introduce el denominador: "))

if num2 != 0:
    resultado = num1 / num2
    print("El resultado de la división es:", resultado)
else:
    print("Error: no se puede dividir entre 0 😬")
