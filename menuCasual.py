import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import random
import os

#BASE DE DATOS SIMULADA
CATALOGO_PRODUCTOS = [
    ("Coca Cola 500ml", 2.50, 3.00), ("Coca Cola 1.5L", 6.50, 7.50), ("Coca Cola 3L", 10.50, 11.50),
    ("Inca Kola 500ml", 2.50, 3.00), ("Inca Kola 1.5L", 6.50, 7.50), ("Inca Kola 3L", 10.50, 11.50),
    ("Agua San Luis 625ml", 2.00, 2.50), ("Agua San Luis 2.5L", 4.50, 5.00),
    ("Sporade Tropical", 2.50, 3.00), ("Sporade Mandarina", 2.50, 3.00),
    ("Red Bull Lata", 7.00, 8.50), ("Monster Energy", 8.00, 9.50),
    ("Volt Maca", 2.00, 2.50), ("Volt Ginseng", 2.00, 2.50),
    ("Frugos del Valle Durazno", 2.50, 3.00), ("Cifrut 500ml", 1.50, 2.00),
    ("Cerveza Pilsen Lata", 4.50, 5.00), ("SixPack Pilsen", 24.90, 26.90),
    ("Cerveza Cusqueña Trigo", 5.50, 6.00), ("Cerveza Cristal 650ml", 6.00, 6.50),
    ("Ron Cartavio Selecto", 28.00, 32.00), ("Ron Cartavio Black", 35.00, 40.00),
    ("Vodka Russkaya", 22.00, 25.00), ("Whisky Red Label", 55.00, 65.00),
    ("Vino Tabernero Borgoña", 19.90, 22.90), ("Vino Santiago Queirolo", 24.90, 28.90),
    ("Pisco Vargas", 25.00, 30.00), ("Four Loko Gold", 12.00, 14.00),
    ("Smirnoff Ice", 8.00, 9.00), ("Chilcano La Caravedo", 9.00, 10.00),
    ("Papas Lays Clasicas", 1.50, 2.00), ("Papas Lays Grandes", 6.50, 7.50),
    ("Pringles Original Pequena", 7.00, 8.00), ("Pringles Crema Cebolla", 7.00, 8.00),
    ("Doritos Queso", 2.50, 3.00), ("Cheetos Horneados", 2.00, 2.50),
    ("Tortees Picante", 1.50, 2.00), ("Cuates Picante", 1.00, 1.50),
    ("Galleta Oreo Paquete", 2.50, 3.00), ("Galleta Ritz Queso", 1.20, 1.50),
    ("Galleta Morochas", 1.00, 1.20), ("Galleta Soda V", 0.80, 1.00),
    ("Club Social Original", 1.00, 1.20), ("Chokis", 1.50, 2.00),
    ("Chocolate Sublime", 2.00, 2.50), ("Chocolate Triangulo", 2.00, 2.50),
    ("Princesa", 2.50, 3.00), ("Cañonazo", 1.00, 1.50),
    ("Mecano", 1.00, 1.50), ("Golpe", 1.00, 1.20),
    ("Doña Pepa", 1.50, 2.00), ("Cua Cua", 1.00, 1.20),
    ("Caramelos Limon (Bolsa)", 2.00, 3.00), ("Halls Mentol", 1.50, 2.00),
    ("Trident Menta", 2.00, 2.50), ("Chin Chin", 1.00, 1.50),
    ("Empanada de Carne", 3.90, 4.50), ("Empanada de Pollo", 3.90, 4.50),
    ("Empanada Mixta", 3.90, 4.50), ("Sandwich de Pollo", 6.90, 7.50),
    ("Hamburguesa Clasica", 7.90, 8.90), ("Pizza Americana (Personal)", 7.90, 8.90),
    ("Enrollado de Hotdog", 3.50, 4.00), ("Nachos con Queso", 5.00, 6.00),
    ("Cafe Americano 8oz", 2.50, 3.00), ("Cappuccino 8oz", 3.50, 4.00),
    ("Cigarros Lucky Strike (10)", 10.00, 12.00), ("Cigarros Hamilton (20)", 18.00, 20.00),
    ("Cigarros Pall Mall", 15.00, 17.00), ("Encendedor Bic", 2.00, 3.00),
    ("Hielo Bolsa 2Kg", 4.50, 5.50), ("Preservativos Piel", 3.50, 5.00),
    ("Papel Higienico Suave", 2.00, 2.50), ("Pilas AA Par", 5.00, 6.00),
    ("Shampoo Pantene Sachet", 1.50, 2.00), ("Jabon Bolivar", 3.00, 3.50)
]

lista_ventas = []

ventana_principal = Tk()
ventana_principal.title("Gestion de Ventas - TAMBO+")
ventana_principal.geometry("1150x700") 
ventana_principal.config(bg="#F3E5F5") 

#ALGORITMOS Y LOGICA
def ordenar_burbuja(criterio):
    cantidad = len(lista_ventas)
    for i in range(cantidad):
        for j in range(0, cantidad - i - 1):
            if lista_ventas[j][criterio] > lista_ventas[j+1][criterio]:
                lista_ventas[j], lista_ventas[j+1] = lista_ventas[j+1], lista_ventas[j]
    messagebox.showinfo("Ordenamiento", f"Lista ordenada por {criterio}.")
    mostrar_vista_inventario() 

def algoritmo_quicksort(lista, clave):
    if len(lista) <= 1:
        return lista
    else:
        pivote = lista[0]
        menores = [x for x in lista[1:] if x[clave] <= pivote[clave]]
        mayores = [x for x in lista[1:] if x[clave] > pivote[clave]]
        return algoritmo_quicksort(menores, clave) + [pivote] + algoritmo_quicksort(mayores, clave)

def sumar_ventas_recursivo(lista, indice=0):
    if indice == len(lista):
        return 0
    else:
        sub = lista[indice]['precio'] * lista[indice]['cantidad']
        return sub + sumar_ventas_recursivo(lista, indice + 1)

def centrar_ventana(ventana, ancho, alto):
    pantalla_ancho = ventana.winfo_screenwidth()
    pantalla_alto = ventana.winfo_screenheight()
    x = int((pantalla_ancho / 2) - (ancho / 2))
    y = int((pantalla_alto / 2) - (alto / 2))
    ventana.geometry(f"{ancho}x{alto}+{x}+{y}")

#VISTAS DEL PANEL DERECHO
def limpiar_panel():
    for widget in panel_derecho.winfo_children():
        widget.destroy()

# --- VISTA BIENVENIDA ---
def mostrar_vista_bienvenida():
    limpiar_panel()
    Label(panel_derecho, text="BIENVENIDO AL SISTEMA\nTAMBO+", 
          font=("Arial", 32, "bold"), fg="#6A1B9A", bg="white").pack(pady=(100, 20))
    Label(panel_derecho, text="Seleccione una opcion del menu lateral", font=("Arial", 14), fg="#757575", bg="white").pack()

# --- VISTA REGISTRO ---
def mostrar_vista_registro():
    limpiar_panel()
    Label(panel_derecho, text="REGISTRAR NUEVA VENTA", font=("Arial", 20, "bold"), fg="#6A1B9A", bg="white").pack(pady=30)

    marco_form = Frame(panel_derecho, bg="#F3E5F5", padx=40, pady=40)
    marco_form.pack()

    estilo_lbl = {"bg": "#F3E5F5", "fg": "#4A148C", "font": ("Arial", 11, "bold")}
    
    Label(marco_form, text="Codigo:", **estilo_lbl).grid(row=0, column=0, sticky="e", pady=10)
    campo_cod = Entry(marco_form, font=("Arial", 11)); campo_cod.grid(row=0, column=1, padx=10)

    Label(marco_form, text="Producto:", **estilo_lbl).grid(row=1, column=0, sticky="e", pady=10)
    campo_nom = Entry(marco_form, font=("Arial", 11)); campo_nom.grid(row=1, column=1, padx=10)

    Label(marco_form, text="Precio (S/):", **estilo_lbl).grid(row=2, column=0, sticky="e", pady=10)
    campo_pre = Entry(marco_form, font=("Arial", 11)); campo_pre.grid(row=2, column=1, padx=10)

    Label(marco_form, text="Cantidad:", **estilo_lbl).grid(row=3, column=0, sticky="e", pady=10)
    campo_cant = Entry(marco_form, font=("Arial", 11)); campo_cant.grid(row=3, column=1, padx=10)

    # Label para el mensaje de confirmación (oculto al inicio)
    lbl_mensaje = Label(marco_form, text="", bg="#F3E5F5", font=("Arial", 10, "bold"))
    lbl_mensaje.grid(row=4, column=0, columnspan=2, pady=5)

    def funcion_aleatoria():
        campo_cod.delete(0, END); campo_nom.delete(0, END)
        campo_pre.delete(0, END); campo_cant.delete(0, END)
        lbl_mensaje.config(text="") # Limpiar mensaje previo
        
        prod_data = random.choice(CATALOGO_PRODUCTOS)
        nombre = prod_data[0]
        min_p, max_p = prod_data[1], prod_data[2]
        
        codigo_final = str(random.randint(1000, 9999))
        for v in lista_ventas:
            if v['descripcion'] == nombre:
                codigo_final = v['codigo']
                break
        
        precio_final = round(random.uniform(min_p, max_p), 2)
        cantidad_final = random.randint(1, 15)
        
        campo_cod.insert(0, codigo_final)
        campo_nom.insert(0, nombre)
        campo_pre.insert(0, str(precio_final))
        campo_cant.insert(0, str(cantidad_final))

    def guardar():
        try:
            cod = campo_cod.get()
            nom = campo_nom.get()
            if not cod or not nom:
                messagebox.showwarning("Aviso", "Faltan datos.")
                return
            
            for v in lista_ventas:
                if v['codigo'] == cod and v['descripcion'] != nom:
                    messagebox.showerror("Error", f"El codigo {cod} ya pertenece a '{v['descripcion']}'")
                    return

            nueva = {'codigo': cod, 'descripcion': nom, 'precio': float(campo_pre.get()), 'cantidad': int(campo_cant.get())}
            lista_ventas.append(nueva)
            
            # --- MODIFICACIÓN: MENSAJE EN LABEL EN LUGAR DE POPUP ---
            lbl_mensaje.config(text="Venta registrada correctamente", fg="#2E7D32") # Texto Verde
            
            # Limpiar campos
            campo_cod.delete(0, END); campo_nom.delete(0, END)
            campo_pre.delete(0, END); campo_cant.delete(0, END)
            
        except ValueError:
            messagebox.showerror("Error", "Revise los numeros.")

    botones = Frame(marco_form, bg="#F3E5F5")
    botones.grid(row=5, column=0, columnspan=2, pady=15)
    Button(botones, text="Generar Aleatorio", command=funcion_aleatoria, bg="#9C27B0", fg="white", font=("Arial", 10, "bold")).pack(side=LEFT, padx=5)
    Button(botones, text="GUARDAR", command=guardar, bg="#FFD600", fg="black", font=("Arial", 11, "bold"), width=15).pack(side=LEFT, padx=5)

# --- VISTA INVENTARIO ---
def mostrar_vista_inventario(datos=None):
    limpiar_panel()
    Label(panel_derecho, text="INVENTARIO DE TIENDA", font=("Arial", 20, "bold"), fg="#6A1B9A", bg="white").pack(pady=20)

    marco_tabla = Frame(panel_derecho, bg="white")
    marco_tabla.pack(fill=BOTH, expand=True, padx=40, pady=(0, 40))

    cols = ('codigo', 'descripcion', 'precio', 'cantidad', 'total')
    tabla = ttk.Treeview(marco_tabla, columns=cols, show='headings')

    estilo = ttk.Style()
    estilo.theme_use("clam")
    estilo.configure("Treeview.Heading", background="#FFD600", foreground="black", font=("Arial", 11, "bold"))
    estilo.configure("Treeview", rowheight=25)

    headers = ['Codigo', 'Producto', 'Precio', 'Cant.', 'Total']
    widths = [80, 280, 80, 60, 100]
    for c, h, w in zip(cols, headers, widths):
        tabla.heading(c, text=h); tabla.column(c, width=w, anchor="center")
    tabla.column('descripcion', anchor="w")

    scrolly = ttk.Scrollbar(marco_tabla, orient=VERTICAL, command=tabla.yview)
    tabla.configure(yscroll=scrolly.set)
    scrolly.pack(side=RIGHT, fill=Y)
    tabla.pack(side=LEFT, fill=BOTH, expand=True)

    lista_final = datos if datos is not None else lista_ventas
    for v in lista_final:
        tot = v['precio'] * v['cantidad']
        tabla.insert('', END, values=(v['codigo'], v['descripcion'], f"S/ {v['precio']}", v['cantidad'], f"S/ {tot:.2f}"))

# --- VISTA BUSCAR ---
def mostrar_vista_buscar():
    limpiar_panel()
    Label(panel_derecho, text="BUSCADOR DE PRODUCTOS", font=("Arial", 20, "bold"), fg="#6A1B9A", bg="white").pack(pady=20)
    
    marco_bus = Frame(panel_derecho, bg="white")
    marco_bus.pack(fill=X, padx=40)
    Label(marco_bus, text="Escriba para filtrar:", bg="white", fg="#757575").pack(anchor="w")
    entrada = Entry(marco_bus, font=("Arial", 14), bg="#F3E5F5", bd=2, relief="groove")
    entrada.pack(fill=X, pady=5)
    
    marco_res = Frame(panel_derecho, bg="white")
    marco_res.pack(fill=BOTH, expand=True, padx=40, pady=20)

    cols = ('codigo', 'descripcion', 'precio', 'cantidad')
    tabla = ttk.Treeview(marco_res, columns=cols, show='headings')
    tabla.heading('codigo', text='Codigo'); tabla.column('codigo', width=80)
    tabla.heading('descripcion', text='Producto'); tabla.column('descripcion', width=250)
    tabla.heading('precio', text='Precio'); tabla.column('precio', width=80)
    tabla.heading('cantidad', text='Cant.'); tabla.column('cantidad', width=60)
    tabla.pack(fill=BOTH, expand=True)

    def filtrar(e):
        txt = entrada.get().lower()
        for item in tabla.get_children(): tabla.delete(item)
        for v in lista_ventas:
            if txt in v['codigo'].lower() or txt in v['descripcion'].lower():
                tabla.insert('', END, values=(v['codigo'], v['descripcion'], f"S/ {v['precio']}", v['cantidad']))
    filtrar(None)
    entrada.bind("<KeyRelease>", filtrar)

# --- VISTA ESTADISTICAS ---
def mostrar_vista_estadisticas():
    limpiar_panel()
    Label(panel_derecho, text="REPORTE DE VENTAS", font=("Arial", 20, "bold"), fg="#6A1B9A", bg="white").pack(pady=15)

    if not lista_ventas:
        Label(panel_derecho, text="Sin ventas registradas.", font=("Arial", 14), bg="white").pack()
        return

    # Calculos
    total_dinero = sum(v['precio'] * v['cantidad'] for v in lista_ventas)
    promedio = total_dinero / len(lista_ventas)
    
    top_mas = sorted(lista_ventas, key=lambda x: x['cantidad'], reverse=True)[:5]
    top_menos = sorted(lista_ventas, key=lambda x: x['cantidad'])[:5]

    marco_resumen = Frame(panel_derecho, bg="#E1BEE7", padx=10, pady=10)
    marco_resumen.pack(fill=X, padx=40, pady=5)
    Label(marco_resumen, text=f"TOTAL ACUMULADO: S/ {total_dinero:,.2f}   |   TICKET PROMEDIO: S/ {promedio:,.2f}", 
          bg="#E1BEE7", fg="#4A148C", font=("Arial", 12, "bold")).pack()

    # Contenedor tablas
    contenedor_tablas = Frame(panel_derecho, bg="white")
    contenedor_tablas.pack(fill=BOTH, expand=True, padx=30, pady=10)

    def crear_tabla_top(padre, titulo, color_fondo, datos):
        frame = Frame(padre, bg="white", bd=1, relief="solid")
        frame.pack(side=LEFT, fill=BOTH, expand=True, padx=10, pady=5)
        
        Label(frame, text=titulo, bg=color_fondo, fg="white", font=("Arial", 11, "bold"), pady=5).pack(fill=X)
        
        cols = ('prod', 'cant')
        t = ttk.Treeview(frame, columns=cols, show='headings', height=5)
        
        t.heading('prod', text='Producto'); t.column('prod', width=180)
        t.heading('cant', text='Cant.'); t.column('cant', width=50, anchor="center")
        t.pack(fill=BOTH, expand=True, padx=5, pady=5)
        
        for d in datos:
            t.insert('', END, values=(d['descripcion'], d['cantidad']))

    crear_tabla_top(contenedor_tablas, "TOP 5 MAS VENDIDOS", "#2E7D32", top_mas)
    crear_tabla_top(contenedor_tablas, "MENOS VENDIDOS", "#C62828", top_menos)

# --- VISTA TOTAL ---
def mostrar_vista_total():
    limpiar_panel()
    Label(panel_derecho, text="CIERRE DE CAJA", font=("Arial", 20, "bold"), fg="#6A1B9A", bg="white").pack(pady=30)
    if not lista_ventas:
        Label(panel_derecho, text="Caja vacia.", font=("Arial", 14), bg="white").pack()
        return
    total = sumar_ventas_recursivo(lista_ventas)
    marco = Frame(panel_derecho, bg="#FFD600", padx=60, pady=40)
    marco.pack()
    Label(marco, text="TOTAL RECAUDADO", bg="#FFD600", fg="black", font=("Arial", 12)).pack()
    Label(marco, text=f"S/ {total:,.2f}", bg="#FFD600", fg="black", font=("Arial", 40, "bold")).pack(pady=10)
    Label(marco, text="(Calculo Recursivo)", bg="#FFD600", fg="#333", font=("Arial", 9)).pack()

#POPUP ORDENAR
def popup_ordenar():
    if not lista_ventas:
        messagebox.showwarning("Aviso", "No hay ventas.")
        return
    win = Toplevel(ventana_principal)
    win.title("Ordenar")
    centrar_ventana(win, 300, 300)
    win.config(bg="#6A1B9A")

    Label(win, text="ORDENAR POR:", fg="#FFD600", bg="#6A1B9A", font=("Arial", 14, "bold")).pack(pady=20)
    
    def call_qs(criterio):
        global lista_ventas
        lista_ventas = algoritmo_quicksort(lista_ventas, criterio)
        win.destroy()
        mostrar_vista_inventario()

    btn_style = {"bg": "white", "fg": "black", "font": ("Arial", 10, "bold"), "width": 25}
    Button(win, text="Precio (Burbuja)", command=lambda: [ordenar_burbuja('precio'), win.destroy()], **btn_style).pack(pady=5)
    Button(win, text="Codigo (QuickSort)", command=lambda: call_qs('codigo'), **btn_style).pack(pady=5)
    Button(win, text="Cantidad (QuickSort)", command=lambda: call_qs('cantidad'), **btn_style).pack(pady=5)

# INICIO
barra = Frame(ventana_principal, bg="#6A1B9A", width=280)
barra.pack(fill="y", side="left")
barra.pack_propagate(False)

# Logo
try:
    ruta = os.path.join(os.path.dirname(os.path.abspath(__file__)), "logo_tambo.png")
    pil_img = Image.open(ruta)
    base = 160
    w_p = (base / float(pil_img.size[0]))
    h_size = int((float(pil_img.size[1]) * float(w_p)))
    pil_img = pil_img.resize((base, h_size), Image.Resampling.LANCZOS)
    tk_img = ImageTk.PhotoImage(pil_img)
    Label(barra, image=tk_img, bg="#6A1B9A").pack(pady=30)
except:
    Label(barra, text="TAMBO+", fg="#FFD600", bg="#6A1B9A", font=("Arial", 26, "bold")).pack(pady=40)

def btn_menu(txt, cmd):
    return Button(barra, text=txt, command=cmd, bg="#FFD600", fg="black", font=("Arial", 11, "bold"), relief="raised", bd=3, cursor="hand2", width=22)

btn_menu("Registrar Venta", mostrar_vista_registro).pack(pady=8)
btn_menu("Ver Inventario", mostrar_vista_inventario).pack(pady=8)
btn_menu("Ordenar Lista", popup_ordenar).pack(pady=8)
btn_menu("Buscar Producto", mostrar_vista_buscar).pack(pady=8)
btn_menu("Reporte Ventas", mostrar_vista_estadisticas).pack(pady=8)
btn_menu("Cierre de Caja", mostrar_vista_total).pack(pady=8)

Frame(barra, bg="#6A1B9A", height=50).pack(side=BOTTOM)
Button(barra, text="SALIR", command=ventana_principal.quit, bg="#D32F2F", fg="white", font=("Arial", 10, "bold"), width=20).pack(side=BOTTOM, pady=20)

panel_derecho = Frame(ventana_principal, bg="white")
panel_derecho.pack(fill="both", expand=True)

mostrar_vista_bienvenida()
ventana_principal.mainloop()