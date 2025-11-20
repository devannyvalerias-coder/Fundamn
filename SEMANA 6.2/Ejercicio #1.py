print("Ejercicios try except - Jueves 20 de nov\n")

print("Ejercicio 1: Convertir texto a número\n")

try:
    edad = int(input("¿Cuántos años tienes? "))
    print(f"El próximo año tendrás {edad + 1}")
except ValueError:
    print("ERROR: Debes escribir un número, no texto")