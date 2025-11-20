print("Ejercicios try except - Jueves 20 de nov\n")

print("Ejercicio 2: División entre números\n")

try:
    numero1 = int(input("Escribe el primer número: "))
    numero2 = int(input("Escribe el segundo número: "))
    resultado = numero1 / numero2
    print(f"El resultado de {numero1} / {numero2} = {resultado}")
except ZeroDivisionError:
    print("ERROR: No puedes dividir entre cero")
except ValueError:
    print("ERROR: Debes escribir números, no texto")