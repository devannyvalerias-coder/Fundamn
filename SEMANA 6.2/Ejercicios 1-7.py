print("Ejercicios diccionarios - martes (n°)")
print("Ejercicio 1\n")

# Escribe tus datos
usuario = {
    "nombre": "Valeria",
    "edad": 18,
    "ciudad": "Monterrey"
}

print("Diccionario completo:")
print(usuario)

print("\nAcceso a valores individuales:")
print("Nombre:", usuario["nombre"])
print("Edad:", usuario["edad"])
print("Ciudad:", usuario["ciudad"])

print("\nEjercicio 2\n")
# Diccionario inicial
videojuego = {
    "título": "Minecraft",
    "plataforma": "PC"}
print("Diccionario original:")
print(videojuego)

# Agregar nuevos datos
videojuego["año"] = 2011
videojuego["género"] = "Sandbox"
videojuego["es_multijugador"] = True
videojuego["precio"] = "Gratis"

print("\nDiccionario después de agregar datos:")
print(videojuego)

print("\nNuevos datos agregados:")
print("Año:", videojuego["año"])
print("Género:", videojuego["género"])
print("Precio:", videojuego["precio"])
print("¿Es multijugador?:", videojuego["es_multijugador"]) 

print("\nEjercicio 3\n")
# Agrega tus datos
perfil = {
    "usuario": "Valeria",
    "seguidores": 500,
    "publicaciones": 25,
    "ciudad": "Monterrey"
}

print("Perfil original:")
print(perfil)

print("Seguidores antes:", perfil["seguidores"])

# Modificar valores (gana más seguidores)
perfil["seguidores"] = 1250
perfil["publicaciones"] = 45

print("\nPerfil actualizado:")
print(perfil)

print("Seguidores ahora:", perfil["seguidores"])
print("Publicaciones ahora:", perfil["publicaciones"])

print("\nEjercicio 4 - eliminar un par clave-valor\n")
# Escribe tus datos
cuenta = {
    "usuario": "pon tu usuario",
    "email": "agrega tu email",
    "telefono": "escribe tu numero",
    "ciudad": "pon tu ciudad"
}

print("Cuenta original (con teléfono):")
print(cuenta)

# Eliminar el número de teléfono por privacidad
del cuenta["telefono"]

print("\nCuenta después de eliminar teléfono:")
print(cuenta)

# Verificación
print("\nVerificación - ¿existe 'telefono'? :", "telefono" in cuenta)

print("\nEjercicio 5 - len\n")

# Agrega tu propia película
pelicula = {
    "título": "Avatar",
    "director": "James Cameron",
    "año": 2009,
    "género": "Ciencia Ficción",
    "duración_minutos": 162,
    "calificación": 8.0
}

print("Película:")
print(pelicula)

# Contar cuántos elementos tiene el diccionario
cantidad = len(pelicula)

print("\n¿Cuántos datos tiene el diccionario?:", cantidad)
print("El diccionario tiene", cantidad, "pares clave-valor")

print("\nEjercicio 6 - obtener las keys\n")
# Agrega tu canción favorita
cancion = {
    "título": "deja vu",
    "artista": "Olivia Rodrigo",
    "album": "GUTS",
    "año": 2023,
    "género": "Pop rock",
    "duración_segundos": 300
}

print("Diccionario de canción:")
print(cancion)

print("\nTodas las claves o datos del diccionario:")
claves = cancion.keys()
print(claves)

print("\nEjercicio 6 - obtener las keys\n")
# Agrega tu canción favorita
cancion = {
    "título": "deja vu",
    "artista": "Olivia Rodrigo",
    "album": "GUTS",
    "año": 2023,
    "género": "Pop rock",
    "duración_segundos": 300
}

print("Diccionario de canción:")
print(cancion)

print("\nTodas las claves o datos del diccionario:")
claves = cancion.keys()
print(claves)

print("\nEjercicio 7: obtener los values")
calificaciones = {
    "Economia": 8.5,
    "Derecho de aduanas": 9.0,
    "Admin de negocios": 8.0,
    "Logistica y cadena de suministro": 7.5,
    "Mercadotecnia Internacional": 9.5
}

print("Diccionario de calificaciones:")
print(calificaciones)

print("\nTodos los valores del diccionario:")
valores = calificaciones.values()
print(valores)