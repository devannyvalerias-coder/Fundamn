# Ejercicio 1 
# SALIDA - Bienvenida
print ("="*45)
print(" BIENVENIDO A GAME STORE ")
print ("="*45)
print ()

# ENTRADA - Datos del cliente
nombre = input("Ingrese su nombre:")
edad = int(input("Ingrese su edad:"))
# PROCESAMIENTO - Precios fijos de los juegos
precio_fifa = 899.00
precio_cod = 1299.00
precio_hello_kitty = 599.00

# SALIDA - Catalogo de productos
print("------- CATALOGO DE PRODUCTOS -------")
print("1. FIFA 2025 - $" + str(precio_fifa))
print("2. Call of Duty - $" + str(precio_cod))
print("3. Hello Kitty Island Adventure - $" + str(precio_hello_kitty))
print()

# ENTRADA - cantidad de cada juego
cantidad_fifa = float (input(" cuantos FIFA 2025 quieres? "))
cantidad_cod = float (input(" cuantos Call Of Dutty quieres? "))
cantidad_hello_kitty = float (input(" cuantos Hello Kitty Island Adventure quieres? "))

# PROCESAMIENTO - Calculos por juego
total_fifa = precio_fifa * cantidad_fifa
total_cod = precio_cod * cantidad_cod
total_hello_kitty = precio_hello_kitty * cantidad_hello_kitty

# PROCESAMIENTO - Calculos totales 
subtotal = total_fifa + total_cod + total_hello_kitty
iva = subtotal * 0.16
total = subtotal + iva

# PRICESAMIENTO - Cantidad total de juegos
cantidad_total_juegos = cantidad_fifa + cantidad_cod + cantidad_hello_kitty

# PROCESAMIENTO - Crear ticket
print("TICKET DE COMPRA")
print("="*45)
print("Cliente: " + nombre)
print("Edad: " + str(edad) + " años")
print("-"*45)
print("DETALLE DE COMPRA:")
print("FIFA2025:")
print(" Cantidad: " + str(cantidad_fifa))
print(" Precio unitario: $" + str(precio_fifa))
print(" Total: $" + str(total_fifa))
print("Call of Duty:")
print(" Cantidad: " + str(cantidad_cod))
print(" Precio unitario: $" + str(precio_cod))
print(" Total: $" + str(total_cod))
print("Hello Kitty Island Adventure:")
print(" Cantidad: " + str(cantidad_hello_kitty))
print(" Precio unitario: $" + str(precio_hello_kitty))
print(" Total: $" + str(total_hello_kitty))
print("-"*45)
print("Cantidad total de juegos: " + str(cantidad_total_juegos))
print("Subtotal: $" + str(subtotal))
print("IVA (16%): $" + str(iva))
print("="*45)
print("TOTAL A PAGAR: $" + str(total))
print ()
# SALIDA - Mensaje de despedida
print("Gracias por su compra, " + nombre + ". ¡Vuelva pronto!")











# EJEMPLO 1 - CONTROL DE ACCCESO A VIDEOJUEGOS
print("="*22)
print("Ejercicio 1\n")

edad = int(16)

if edad >= 16:
    print("Acceso permitido a todos los videojuegos.")
else:
    print("Acceso restringido a videojuegos para adultos.")


# EJEMPLO 2 - CALCULADORA DE PROMEDIO ESCOLAR
print("Ejercicio 2 con AND\n")

calificacion = int(input("Ingrese su calificación (0-100): "))

if calificacion >= 90 and calificacion <= 100:
    print("Excelente")
elif calificacion >= 80 and calificacion < 90:
    print("Aprobado")
elif calificacion >= 60 and calificacion < -70:
    print("No aprobado")
else:
    print("calificación inválida")
# 3 ejercicios: jugar por edad, calificaciones y calificaciones con rangos usando AND

# ---- Ejercicio 1 ----
print("="*22)
print("Ejercicio 1\n")

# aquí puedes cambiar la edad directamente o usar input()
# edad = int(input("Ingresa tu edad: "))
edad = int(16)  # como en la foto, ejemplo con 16

if edad >= 16:
    print("👍 Podes jugar \n")
else:
    print("👎 No podes jugar \n")

print("-"*18)
# ---- Ejercicio 2 ----
print("Ejercicio 2\n")

# si quieres usar input, descomenta la línea de abajo:
# calificacion = int(input("Ingresa tu calificación (0-100): "))
calificacion = int(input("Ingresa tu calificación (0-100): "))

if calificacion >= 90:
    print("🏆 Excelente")
elif calificacion >= 70:
    print("👍 Aprobado")
else:
    print("😕 Ay!, no aprobado")

print("\n# Ejercicio 2 con AND")
# ---- Ejercicio 2 con AND (rangos más explícitos) ----
# calificacion = int(input("Ingresa tu calificación (0-100): "))
calificacion = int(input("Ingresa tu calificación (0-100): "))

if calificacion >= 90 and calificacion <= 100:
    print("🏆 Excelente")
elif calificacion >= 70 and calificacion < 90:
    print("👍 Aprobado")
elif calificacion >= 0 and calificacion < 70:
    print("😕 Ay!, no aprobado")
else:
    print("🔎 Calificación inválida (debe ser 0-100)")
    
    # recomendador_peliculas.py
# Recomienda películas según la edad y el género

def recomendar_pelicula():
    try:
        edad = int(input("¿Cuál es tu edad? "))
    except ValueError:
        print("Por favor ingresa un número para la edad.")
        return

    genero = input("¿Cuál es tu género favorito? (acción, comedia, terror): ").lower().strip()

    if edad < 13:
        print("Te recomendamos películas infantiles")
        return

    # Para adolescentes (13-17)
    if 13 <= edad <= 17:
        if genero == "acción":
            print("Te recomendamos: Spider-Man (PG-13)")
        elif genero == "comedia":
            print("Te recomendamos: Shrek (PG-13)")
        elif genero == "terror":
            print("Te recomendamos: Scary Stories (PG-13)")
        else:
            print("Género no reconocido. Prueba con acción, comedia o terror.")
        return

    # Para adultos (18+)
    if edad >= 18:
        if genero == "acción":
            print("Te recomendamos: John Wick")
        elif genero == "comedia":
            print("Te recomendamos: Superbad")
        elif genero == "terror":
            print("Te recomendamos: El Conjuro")
        else:
            print("Género no reconocido. Prueba con acción, comedia o terror.")
        return

if __name__ == "_main_":
    recomendar_pelicula()