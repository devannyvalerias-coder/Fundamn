import tkinter as tk
from tkinter import scrolledtext
from tkinter import simpledialog, messagebox

# Función temporal para botones no implementados
def no_listo(nombre_funcion):
    messagebox.showinfo("Info", f"La función '{nombre_funcion}' aún no está disponible.")

# =====================================
# INVENTARIO INICIAL DEL FITZONE SPORT
# =====================================

inventario = [
    {"id": "001", "nombre": "Guantes de box", "marca": "Everlast", "talla": "M", "precio": 450, "stock": 12, "descripcion": "Guantes de entrenamiento"},
    {"id": "002", "nombre": "Mancuernas 5kg", "marca": "Nike", "talla": "unica", "precio": 320, "stock": 8, "descripcion": "Mancuernas de 5kg"},
    {"id": "003", "nombre": "Proteina Whey", "marca": "ON", "talla": "1 kg", "precio": 890, "stock": 5, "descripcion": "suplemento proteina"},
    {"id": "004", "nombre": "Tapetede Yoga", "marca": "Reebok", "talla": "unica", "precio": 280, "stock": 15, "descripcion": "Tapete antideslizante"},
    {"id": "005", "nombre": "Tenis deportivos", "marca": "Adidas","talla": "42", "precio": 1200, "stock": 6, "descripcion": "Tenis para correr"},
    {"id": "006", "nombre": "Bandas elásticas", "marca": "Nike", "talla": "Única", "precio": 150, "stock": 20, "descripcion": "Banda para resistencia"},
    {"id": "007", "nombre": "Short deportivo", "marca": "Reebok", "talla": "L", "precio": 220, "stock": 10, "descripcion": "Short ligero para deporte"},
    {"id": "008", "nombre": "Playera dri-fit", "marca": "Nike", "talla": "M", "precio": 250, "stock": 14, "descripcion": "Playera deportiva"},
    {"id": "009", "nombre": "Botella térmica", "marca": "Tupperware", "talla": "500ml", "precio": 300, "stock": 9, "descripcion": "Botella para líquidos"},
    {"id": "010", "nombre": "Tobillera deportiva", "marca": "Adidas", "talla": "Única", "precio": 180, "stock": 7, "descripcion": "Tobillera elástica"}
    
]

ventas_del_dia = 0

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
        texto.insert(tk.END, f"{item['id']:<5} {item['nombre']:<25} {precio_formateado:<12} {item['talla']:<8} {item['marca']:<15} {item['stock']:<6}\n")

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
        for iten in agotados:
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
            messagebox.showerror("Error", "Cantidad inválida. Debe ser un número mayor a 0.")
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
    messagebox.showinfo("Éxito", f"Producto '{nombre}' agregado correctamente. ")
    mostrar_inventario()
                    
# ===========================================
# INTERFAZ PRINCIPAL
# ===========================================

ventana = tk.Tk()
ventana.title("FITZONE SPORT - Sistema de Inventario y Ventas")
ventana.geometry("1200x800")
ventana.configure(bg="white")

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
    ("VENDER", lambda: no_listo("Vender producto")),
    ("BUSCAR", lambda: no_listo("Buscar productos"))
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

# -------------------------------------
# Mostrar HOME al iniciar
# -------------------------------------

mostrar_home()

ventana.mainloop()