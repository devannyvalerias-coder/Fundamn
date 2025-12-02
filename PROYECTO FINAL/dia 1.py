import tkinter as tk
from tkinter import scrolledtext

# =====================================
# INVENTARIO INICIAL DEL FITZONE SPORT
# =====================================

inventario = [
    {"nombre": "Guantes de box", "stock": 12, "precio": 450},
    {"nombre": "Mancuernas 5kg", "stock": 8, "precio": 320},
    {"nombre": "Proteína Whey", "stock": 5, "precio": 890},
    {"nombre": "Tapete de yoga", "stock": 15, "precio": 280},
    {"nombre": "Tenis deportivos", "stock": 6, "precio": 1200},
    {"nombre": "Bandas elásticas", "stock": 20, "precio": 150},
    {"nombre": "Short deportivo", "stock": 10, "precio": 220},
    {"nombre": "Playera dri-fit", "stock": 14, "precio": 250},
    {"nombre": "Botella térmica", "stock": 9, "precio": 300},
    {"nombre": "Tobillera deportiva", "stock": 7, "precio": 180}
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

def no_listo(nombre):
    texto.delete(1.0, tk.END)
    texto.insert(tk.END, f"La función '{nombre}' estará disponible en el Día 2.\n")

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
    ("INVENTARIO", lambda: no_listo("Inventario")),
    ("AGREGAR", lambda: no_listo("Agregar producto")),
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