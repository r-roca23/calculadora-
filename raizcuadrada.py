import math

# Calculadora de raíces cuadradas

print("=== Calculadora de Raíz Cuadrada ===")

numero = float(input("Ingresa un número: "))

if numero < 0:
    print("No se puede calcular la raíz cuadrada de un número negativo.")
else:
    resultado = math.sqrt(numero)
    print("La raíz cuadrada es:", resultado)

