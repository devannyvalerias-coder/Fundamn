#Lydia Ortiz AL07182129
#Valeria Maya AL07003865
# Programa: Cálculo de boletos para el Museo
#tabla de la verdad
print("\nPrecios de entrada")
print("====================")
print("El adulto mayor paga $45")
print("Un Profesor paga $45")
print("Un Estudiante paga $30")
print("========================")
print("\n           Descuentos")
print("=======================")
print("El descuento para un adulto mayor es %0.12")
print("El descuento para un profesor es %0.10")
print("El descuento para un estudiante es %0.10")

# Tabla de descuentos
descuentos = {
    "adulto mayor": 0.12,
    "profesor": 0.10,
    "estudiante": 0.10,
    "ninguno": 0.0
}

print("Bienvenido a tu calculadora de precios para el Museo")

# Pedimos cuántos visitantes van a pagar
num_visitantes = int(input("¿Cuántos visitantes pagarán boleto? "))

total = 0  # acumulador del costo total

for i in range(num_visitantes):
    print("\nVisitante", i+1)

    edad = int(input("Ingrese la edad: "))

    # Menores de 3 años no pagan
    if edad < 3:
        print("Este visitante entra gratis")
        continue

    # Precio base según edad
    if edad < 18:
        precio = 30
    else:
        precio = 45

    print("Precio base: $", precio)

    # Preguntar tipo de visitante
    print("Tipos: adulto mayor / profesor / estudiante / ninguno")
    tipo = input("Escriba la ocupacion de visitante: ")

    # Si no se escribe bien, no hay descuento
    if tipo not in descuentos:
        print("Dato incorrecto, no se aplica descuento")
        tipo = "ninguno"

    # Aplicar descuento
    descuento = descuentos[tipo]
    precio_final = precio - (precio * descuento)

    if descuento > 0:
        print("Se uso un descuento de", int(descuento*100), "%")

    print("Precio final: $", round(precio_final, 2))

    total = total + precio_final

    # Break obligatorio
    if total > 500:
        print("El total supera los $500, se termina el cálculo")
        break

# Mostrar resultado final
print("El total a pagar es: $", round(total, 2))
print("Muchas gracias por su compra, disfruten su estadia en el Museo")
