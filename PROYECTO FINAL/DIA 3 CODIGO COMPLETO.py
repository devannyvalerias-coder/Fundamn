import time
import tkinter as tk
from tkinter import scrolledtext
from tkinter import simpledialog, messagebox
from datetime import datetime

# ===================================================
# INICIO DE SESIÓN DEL USUARIO CON TKINTER
# ===================================================

def solicitar_usuario_tk():
    """Abre cuadros de dialogo para pedir nombre, nickname y fecha antes de mostrar el menú."""

    nombre = simpledialog.askstring("Inicio de sesión", "Por favor, ingresa nombre: ")
    if not nombre:
        messagebox.showerror("Error", "Debes ingresar un nombre.")
        return solicitar_usuario_tk()
    
    nickname = simpledialog.askstring("Inicio de sesion", "Ingresa tu nickname:")
    if not nickname:
        messagebox.showerror("Error", "Debes ingresar un nickname.")
        return solicitar_usuario_tk()
    
    while True:
        fecha = simpledialog.askstring("Inicio de sesión", "Ingresa la fecha (DD/MM/AAAA):")
        if not fecha:
            messagebox.showerror("Error", "Debes ingresar la fecha.")
            continue

        try:
            # Intentar convertir la fecha
            dia, mes, anio = map(int, fecha.split("/"))
            fecha_tupla = (dia, mes, anio)

            # validar que sea una fecha REAL
            datetime(anio, mes, dia)
            break
        except:
            messagebox.showerror("Error", "formato inválido o fecha inexistente. \nEjemplo válido: 25/11/24")

    # --- MENSAJE DE ÉXITO --- 
    messagebox.showinfo(
    "Registro exitoso",
    f"Bienvenido/a {nombre} ({nickname})\nFecha: {dia}/{mes}/{anio}\nRegistro completado."
    )

    return nombre, nickname, fecha_tupla


# =====================================
# INVENTARIO INICIAL DEL FITZONE SPORT
# =====================================

inventario = [
    {"id": "001", "nombre": "Guantes de box", "marca": "Everlast", "talla": "M", "precio": 450, "stock": 12, "descripcion": "Guantes de entrenamiento"},
    {"id": "002", "nombre": "Mancuernas 5kg", "marca": "Nike", "talla": "unica", "precio": 320, "stock": 8, "descripcion": "Mancuernas de 5kg"},
    {"id": "003", "nombre": "Proteina Whey", "marca": "ON", "talla": "1 kg", "precio": 890, "stock": 5, "descripcion": "suplemento proteina"},
    {"id": "004", "nombre": "Tapete Yoga", "marca": "Reebok", "talla": "unica", "precio": 280, "stock": 15, "descripcion": "Tapete antideslizante"},
    {"id": "005", "nombre": "Tenis deportivos", "marca": "Adidas","talla": "42", "precio": 1200, "stock": 6, "descripcion": "Tenis para correr"},
    {"id": "006", "nombre": "Bandas elásticas", "marca": "Nike", "talla": "Única", "precio": 150, "stock": 20, "descripcion": "Banda para resistencia"},
    {"id": "007", "nombre": "Short deportivo", "marca": "Reebok", "talla": "L", "precio": 220, "stock": 10, "descripcion": "Short ligero para deporte"},
    {"id": "008", "nombre": "Playera dri-fit", "marca": "Nike", "talla": "M", "precio": 250, "stock": 14, "descripcion": "Playera deportiva"},
    {"id": "009", "nombre": "Botella térmica", "marca": "Tupperware", "talla": "500ml", "precio": 300, "stock": 9, "descripcion": "Botella para líquidos"},
    {"id": "010", "nombre": "Tobillera deportiva", "marca": "Adidas", "talla": "Única", "precio": 180, "stock": 7, "descripcion": "Tobillera elástica"}
    
]
# ==================================
# VARIABLES DEL DIA 3
# ==================================

ventas_del_dia = 0
historial_ventas = []

# ===================================
# FUNCIONES DEL MENU
# ===================================

def mostrar_home():
    texto.delete(1.0, tk.END)

    total_modelos = len(inventario)
    total_stock = sum(item["stock"] for item in inventario)
    alertas = [item["nombre"] for item in inventario if item["stock"] <= 5]

    ascii_art = """
===================================

     F I T Z O N E    S P O R T 

================================== 
"""

    texto.insert(tk.END, ascii_art + "\n")
    texto.insert(tk.END, f"Total de modelos únicos: {total_modelos}\n")
    texto.insert(tk.END, f"Total de productos en stock: {total_stock}\n")
    texto.insert(tk.END, f"Ventas realizadas hoy: {ventas_del_dia}\n\n")

    if alertas:
        texto.insert(tk.END, "Productos con stock bajo:\n", "alerta")
        for item in alertas:
            texto.insert(tk.END, f" - {item}\n", "alerta")

    else:
        texto.insert(tk.END, "No hay alertas de stock bajo.\n")
# ------------------------------
# FUNCION DE INVENTARIO
# -----------------------------

def mostrar_inventario():
    texto.delete(1.0, tk.END)
    texto.insert(tk.END, f"{'ID':5} {'MODELO':<25} {'PRECIO':<12} {'TALLA':<8} {'MARCA':<15} {'STOCK':<6}\n")
    texto.insert(tk.END, "-"*80 + "\n")

    for item in inventario:
        precio_formateado = "${:,.0f}".format(item["precio"])

        # Si el producto está sin stock, lo mostramos en rojo con etiqueta
        if item["stock"] == 0:
            texto.insert(
                tk.END,
                f"{item['id']:<5} {item['nombre']:<25} {precio_formateado:<12} {item['talla']:<8} {item['marca']:<15} {item['stock']:<6}  <-- AGOTADO\n",
                "alerta"
            )
        else:
            texto.insert(
                tk.END,
                f"{item['id']:<5} {item['nombre']:<25} {precio_formateado:<12} {item['talla']:<8} {item['marca']:<15} {item['stock']:<6}\n"
            )

    texto.insert(tk.END, "\nProductos con stock bajo (<3):\n", "alerta")
    bajos = [item for item in inventario if item["stock"] <= 3 and item["stock"] > 0]
    if bajos:
        for item in bajos:
            texto.insert(tk.END, f" - {item['nombre']} (stock: {item['stock']})\n", "alerta")
    else:
        texto.insert(tk.END, "Ninguno\n", "alerta")

    texto.insert(tk.END, "\nProductos agotados (stock = 0):\n", "alerta")
    agotados = [item for item in inventario if item["stock"] == 0]
    if agotados:
        for item in agotados:
            texto.insert(tk.END, f" - {iten['nombre']}\n", "alerta")
    else:
        texto.insert(tk.END, "Ninguno\n", "alerta")

# -----------------------------------------
# FUNCION GENERAR UN NUEVO ID
# -----------------------------------------
def generar_nuevo_id():
    if inventario:
        max_id = max(int(item["id"]) for item in inventario)
        nuevo_id = "{:03d}".format(max_id +1)
    else:
        nuevo_id = "001"
    return nuevo_id

# ----------------------------------------
# FUNCION AGREGAR PRODUCTO
# ----------------------------------------


def agregar_producto():
    nombre = simpledialog.askstring("Agregar Producto", "Nombre del modelo:")
    if not nombre:
        return

    marca = simpledialog.askstring("Agregar Producto", "Marca:")
    if not marca:
        return
    
    while True:
        try:
            precio = float(simpledialog.askstring("Agregar Producto", "Precio:"))
            if precio <= 0:
                raise ValueError
            break
        except:
            messagebox.showerror("Error", "Precio inválido. Debe ser un numero mayor a 0.")

    talla = simpledialog.askstring("Agregar producto", "Talla:")
    if not talla:
        return
    
    while True:
        try:
            cantidad = int(simpledialog.askstring("Agregar Producto", "Cantidad inicial: "))
            if cantidad <= 0:
                raise ValueError
            break
        except:
            messagebox.showerror("Error", "Cantidad inválida. Debe ser un numero mayor a 0.")

    descripcion = simpledialog.askstring("Agregar producto", "Descripción: ")

    nuevo_producto = {
        "id": generar_nuevo_id(),
        "nombre": nombre,
        "marca": marca,
        "precio": precio,
        "talla": talla,
        "stock": cantidad,
        "descripcion": descripcion
    }

    inventario.append(nuevo_producto)
    messagebox.showinfo("Éxito", f"Productos '{nombre}' agregado correctamente. ")
    mostrar_inventario()

# =================================
# DIA 3 - FUNCION DE VENTAS
# =================================

def vender_producto():
    global ventas_del_dia

    id_buscar= simpledialog.askstring("Vender producto", "Ingrese id del producto:")
    if not id_buscar:
        return
    
    productos = next((p for p in inventario if p["id"] == id_buscar), None)

    if not productos:
        messagebox.showerror("Error", "No existe un producto con este ID.")
        return
    
    if productos["stock"] == 0:
        messagebox.showerror("SIN STOCK", "Este producto está agotado")
        return
    
    while True:
        try:
            cantidad = int(simpledialog.askstring("Venta", "Cantidad a vender:"))
            if cantidad <= 0 or cantidad > productos["stock"]:
                raise ValueError
            break
        except:
            messagebox.showerror("Error", "Cantidad inválida.")

    # Actualizar stock
    productos["stock"] -= cantidad

    # Total de venta
    total = productos["precio"] * cantidad
    ventas_del_dia += total

    # Guardar en historial
    historial_ventas.append({
        "fecha": datetime.now().strftime("%d/%m/%Y %H:%M"),
        "producto": productos["nombre"],
        "cantidad": cantidad,
        "total": total
    })

    # Mostrar recibo en el área del texto
    texto.delete(1.0, tk.END)
    texto.insert(tk.END, "========= RECIBO DE COMPRA =========\n\n")
    texto.insert(tk.END, f"Producto: {productos['nombre']}\n")
    texto.insert(tk.END, f"Cantidad: {cantidad}\n")
    texto.insert(tk.END, f"Precio unitario: ${productos['precio']}\n")
    texto.insert(tk.END, f"TOTAL: ${total}\n\n")
    texto.insert(tk.END, f"Venta realizada correctamente.\n")
    texto.insert(tk.END, "==============================================\n")


    messagebox.showinfo("Venta realizada", "La venta fue registrada exitosamente.")


                    
# ===========================================
# INTERFAZ PRINCIPAL
# ===========================================

ventana = tk.Tk()
ventana.title("FITZONE SPORT - Sistema de Inventario y Ventas")
ventana.geometry("1200x800")
ventana.configure(bg="white")

def buscar_producto():
    texto.delete(1.0, tk.END)

    criterio = simpledialog.askstring("Buscar productos", "ingresa ID o nombre:")
    if not criterio:
        return
    
    criterio = criterio.lower()

    resultados = [
        p for p in inventario
        if criterio in p["id"].lower() or criterio in p["nombre"].lower()
    ]

    if not resultados:
        messagebox.showinfo("Buscar", "No se encontró ningun producto.")
        return
    
    texto.insert(tk.END, "Resultados de búsqueda:\n")
    texto.insert(tk.END, "-"* 60 + "\n")

    
    for p in resultados:
        texto.insert(tk.END,
            f"ID:{p['id']}\n"
            f"Nombre: {p['nombre']}\n"
            f"Marca: {p['marca']}\n"
            f"Talla: {p['talla']}\n"
            f"Precio: {p['precio']}\n"
            f"Stock: {p['stock']}\n"
            f"Descripción: {p['descripcion']}\n"
        )
    

# ===========================================
# BOTONES DEL MENU
# ===========================================

frame_botones = tk.Frame(ventana, bg="white")
frame_botones.pack(pady=20)

def hover(event):
    event.widget.config(bg="blue")

def leave(event):
    event.widget.config(bg="black")

botones_info = [
    ("HOME", mostrar_home),
    ("INVENTARIO", mostrar_inventario),
    ("AGREGAR", agregar_producto),
    ("VENDER", vender_producto),
    ("BUSCAR", buscar_producto)
]

for texto_boton, comando in botones_info:
    boton = tk.Button(
        frame_botones,
        text=texto_boton,
        width=15,
        height=2,
        bg="black",
        fg="white",
        command=comando
    )
    boton.pack(side=tk.LEFT, padx=10)
    boton.bind("<Enter>", hover)
    boton.bind("<Leave>", leave)

# --------------------------------------
# AREA DEL TEXTO CON SCROLL
# --------------------------------------

texto = scrolledtext.ScrolledText(ventana, width=140, height=25, font=("Consolas", 12))
texto.pack(pady=10)

texto.tag_config("alerta", foreground="red")

# --------------------------------------
# FOOTER
# --------------------------------------

footer = tk.Label(
    ventana,
    text="FITZONE SPORT ° Sistema de inventario y Ventas ° Proyecto Final",
    bg="white",
    fg="gray"
)
footer.pack(pady=10)

# ===================================== 
# MOSTRAR LOGIN Y LUEGO EL HOME
# =====================================

def iniciar_programa():
    solicitar_usuario_tk()
    mostrar_home()

ventana.after(100, iniciar_programa)

# ====================================
# INICIAR INTERFAZ
# ====================================


ventana.mainloop()