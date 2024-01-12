import tkinter as tk
import os
from PIL import Image, ImageTk
from realizarCopia import copy 
from volcado import realizarVolcado 
from copiaSeguridad import cSeguridad

def abrir_segunda_ventana():
    global ventana1
    ventana1.destroy()
    segunda_ventana()


def salir():
    global ventana1
    ventana1.destroy()


def abrir_tercera_ventana():
    global ventana2
    ventana2.destroy()
    tercera_ventana()


def abrir_cuarta_ventana():
    global ventana2
    ventana2.destroy()
    cuarta_ventana()


def abrir_quinta_ventana():
    global ventana2
    ventana2.destroy()
    quinta_ventana()


def retroceder_primera_ventana():
    global ventana2
    ventana2.destroy()
    primera_ventana()


def salir_segunda_ventana():
    global ventana2
    ventana2.destroy()
    salir()


def retroceder_segunda_ventana_desde_tercera():
    global ventana3
    ventana3.destroy()
    segunda_ventana()


def retroceder_segunda_ventana_desde_cuarta():
    global ventana4
    ventana4.destroy()
    segunda_ventana()


def retroceder_segunda_ventana_desde_quinta():
    global ventana5
    ventana5.destroy()
    segunda_ventana()


def retroceder_inicio_desde_sexta():
    global ventana6
    ventana6.destroy()
    primera_ventana()


def retroceder_inicio_desde_septima():
    global ventana7
    ventana7.destroy()
    primera_ventana()


def abrir_sexta_ventana_desde_tercera(opcion):
    global ventana3
    ventana3.destroy()
    sexta_ventana(opcion)


def abrir_sexta_ventana_desde_cuarta(opcion):
    global ventana4
    ventana4.destroy()
    sexta_ventana(opcion)


def abrir_sexta_ventana_desde_quinta(opcion):
    global ventana2
    ventana2.destroy()
    sexta_ventana(opcion)


def abrir_septima_ventana_desde_tercera(opcion):
    global ventana3
    ventana3.destroy()
    septima_ventana(opcion)


def abrir_septima_ventana_desde_cuarta(opcion):
    global ventana4
    ventana4.destroy()
    septima_ventana(opcion)


def abrir_septima_ventana_desde_quinta(opcion):
    global ventana2
    ventana2.destroy()
    septima_ventana(opcion)


def llamar_copia(ip1):
    try:
        # Llama al método copy() del módulo realizarCopia.py
        a = copy(ip1)

        if a == 1:
            abrir_sexta_ventana_desde_tercera(1)
        elif a == 2:
            abrir_septima_ventana_desde_tercera(4)
        elif a == 3:
            abrir_septima_ventana_desde_tercera(5)
        elif a == 4:
            abrir_septima_ventana_desde_tercera(6)
    except AttributeError:
        print("El módulo realizarCopia.py no tiene el método copy()")


def llamar_volcado(ip2):
    try:
        # Llama al método copy() del módulo realizarCopia.py
        a = realizarVolcado(ip2)

        if a == 1:
            abrir_sexta_ventana_desde_cuarta(2)
        elif a == 2:
            abrir_septima_ventana_desde_cuarta(2)
    except AttributeError:
        print("El módulo realizarCopia.py no tiene el método copy()")


def llamar_copiaseguridad():
    try:
        # Llama al método copy() del módulo realizarCopia.py
        a = cSeguridad()

        if a == 1:
            abrir_sexta_ventana_desde_quinta(3)
        elif a == 2:
            abrir_septima_ventana_desde_quinta(3)
    except AttributeError:
        print("El módulo realizarCopia.py no tiene el método copy()")

def dar_formato_moderno(widget, color_inicial="gray", color_resaltado="#2980b9", icono=None):
    widget.config(
        font=("Arial", 14),
        foreground="white",  # color del texto
        background=color_inicial,  # color de fondo
        borderwidth=0,  # ancho del borde
        highlightthickness=0  # grosor del resaltado
    )
    widget.bind(
        "<Enter>", lambda event: widget.config(
            background=color_resaltado
        )
    )  # color de fondo al pasar el ratón
    widget.bind(
        "<Leave>", lambda event: widget.config(
            background=color_inicial
        )
    )  # color de fondo al salir el ratón
    widget.config(
        highlightbackground=color_inicial,  # color del borde al inicio
        highlightcolor=color_resaltado  # color del borde al pasar el ratón
    )

    if icono:
        icono_imagen = Image.open(icono)
        icono_imagen = icono_imagen.resize((widget.winfo_reqwidth(), widget.winfo_reqheight()), Image.LANCZOS)
        widget.icono_imagen = ImageTk.PhotoImage(icono_imagen)
        widget.config(image=widget.icono_imagen, compound="right")


def primera_ventana():
    global ventana1
    ventana1 = tk.Tk()
    ventana1.title("¡Bienvenido a moyseafood!")
    ventana1.attributes("-fullscreen", True)

    ventana1.iconbitmap("moyseafood.ico")
    icono_inicio = "icono_inicio.png"
    icono_salir = "icono_salir.png"

    fondo1 = Image.open(os.path.join(os.getcwd(), "moyseafood.png"))
    fondo1 = fondo1.resize(
        (ventana1.winfo_screenwidth(), ventana1.winfo_screenheight()), Image.LANCZOS
    )
    fondo1final = ImageTk.PhotoImage(fondo1)

    canvas = tk.Canvas(ventana1, width=800, height=400)
    canvas.pack(fill="both", expand=True)

    canvas.create_image(0, 0, anchor="nw", image=fondo1final)

    frase_texto = "¡Bienvenido a CopySwift de Moyseafood, pulsa Inicio para comenzar!"
    canvas.create_text(
        ventana1.winfo_screenwidth() // 2,
        ventana1.winfo_screenheight() * 0.8,  # Mover la frase hacia la parte inferior
        text=frase_texto,
        font=("Arial", 16),
        fill="white",
    )

    boton_inicio = tk.Button(
        ventana1, text="Inicio", command=abrir_segunda_ventana
    )
    dar_formato_moderno(boton_inicio, color_inicial="green", color_resaltado="gray", icono=icono_inicio)
    boton_inicio.config(padx=10) 
    boton_inicio.place(relx=0.5, rely=0.9, anchor="center")  # Ubicar el botón en la parte inferior y centrado

    boton_salir = tk.Button(
        ventana1, text="Exit", command=salir
    )
    dar_formato_moderno(boton_salir, color_inicial="red", color_resaltado="gray", icono=icono_salir)
    boton_salir.config(padx=10)
    boton_salir.place(relx=0.95, rely=0.05, anchor="ne")  # Ubicar el botón en la esquina superior derecha

    ventana1.mainloop()



def aperturaprevia_ventana():
    global seleccion
    opcion_seleccionada = seleccion.get()

    if opcion_seleccionada == "Hacer copia de la Base de Datos":
        # Coloca aquí el comando que deseas ejecutar para esta opción
        abrir_tercera_ventana()
        print("Ejecutar comando para la opción 1")
    elif opcion_seleccionada == "Realizar volcado":
        # Coloca aquí el comando que deseas ejecutar para esta opción
        abrir_cuarta_ventana()
        print("Ejecutar comando para la opción 2")
    elif opcion_seleccionada == "Hacer copia de seguridad":
        # Coloca aquí el comando que deseas ejecutar para esta opción
        llamar_copiaseguridad()
        print("Ejecutar comando para la opción 3")


def segunda_ventana():
    global ventana2, seleccion
    ventana2 = tk.Tk()
    ventana2.title("Opciones")
    ventana2.attributes('-fullscreen', True)
    icono_salir = "icono_salir.png"
    icono_retroceder = "icono_retroceder.png"
    icono_inicio = "icono_inicio.png"

    fondo2 = Image.open(os.path.join(os.getcwd(), "moyseafoodsegundaportada.png"))
    fondo2 = fondo2.resize((ventana2.winfo_screenwidth(), ventana2.winfo_screenheight()), Image.LANCZOS)
    fondo2final = ImageTk.PhotoImage(fondo2)

    canvas = tk.Canvas(ventana2, width=800, height=400)
    canvas.pack(fill="both", expand=True)

    canvas.create_image(0, 0, anchor="nw", image=fondo2final)

    frase_texto = "Seleccione la opción que deseas realizar"
    canvas.create_text(
        ventana2.winfo_screenwidth() // 2,
        ventana2.winfo_screenheight() * 0.3,  # Mover la frase hacia la parte inferior
        text=frase_texto,
        font=("Arial", 18),
        fill="white",
    )

    opciones = ["Hacer copia de la Base de Datos", "Realizar volcado", "Hacer copia de seguridad"]
    seleccion = StringVar(ventana2)

    # Ajustar el tamaño del cuadro
    cuadro_opciones = tk.Frame(ventana2, bg="black", padx=25, pady=25)
    cuadro_opciones.place(relx=0.5, rely=0.5, anchor="center")

    for opcion in opciones:
        radio_button = tk.Radiobutton(cuadro_opciones, text=opcion, variable=seleccion, value=opcion, font=("Arial", 14),
                                      bg="white", fg="black", indicatoron=0, selectcolor="green")
        radio_button.pack(fill="both", pady=10, padx=20)

    boton_seleccionar = tk.Button(ventana2, text="Seleccionar", command=aperturaprevia_ventana,
                                  font=("Arial", 14), bg="green", fg="white")
    boton_seleccionar.place(relx=0.5, rely=0.7, anchor="center")

    boton_retroceder = tk.Button(
        ventana2, text="Back", command=retroceder_primera_ventana
    )
    dar_formato_moderno(boton_retroceder, color_inicial="green", color_resaltado="gray", icono=icono_retroceder)
    boton_retroceder.config(padx=10)
    boton_retroceder.place(relx=0.05, rely=0.95, anchor="sw")  # Colocar en la esquina inferior izquierda
   

    boton_salir = tk.Button(
        ventana2, text="Exit", command=salir_segunda_ventana
    )
    dar_formato_moderno(boton_salir, color_inicial="red", color_resaltado="gray", icono=icono_salir)
    boton_salir.config(padx=10)
    boton_salir.place(relx=0.95, rely=0.95, anchor="se")  # Ubicar el botón en la esquina inferior derecha



    
    ventana2.mainloop()



def tercera_ventana():
    global ventana3, fondo
    ventana3 = tk.Tk()
    ventana3.title("Introducir IP")
    ventana3.attributes('-fullscreen',True)
    icono_check = "check.png"
    icono_retroceder = "icono_retroceder.png"
    icono_salir = "icono_salir.png"

    fondo3 = Image.open(os.path.join(os.getcwd(), "moyseafoodsegundaportada.png"))
    fondo3 = fondo3.resize((ventana3.winfo_screenwidth(), ventana3.winfo_screenheight()), Image.LANCZOS)
    fondo3final = ImageTk.PhotoImage(fondo3)

    canvas = tk.Canvas(ventana3, width=800, height=400)
    canvas.pack(fill="both", expand=True)

    canvas.create_image(0, 0, anchor="nw", image=fondo3final)

    frase_texto = "Introduzca la IP de la etiquetadora de la que deseas extraer la Base de Datos"
    canvas.create_text(
        ventana3.winfo_screenwidth() // 2,
        ventana3.winfo_screenheight() * 0.3,  # Mover la frase hacia la parte inferior
        text=frase_texto,
        font=("Arial", 18),
        fill="white",
    )


    entrada_texto = tk.Entry(ventana3, font = ("Arial", 16), width = 20)
    entrada_texto.place(relx=0.5, rely=0.5, anchor="center")

    def comprobar_ip():
        ip1 = entrada_texto.get()
        if  ip1 == "1":
            llamar_copia(ip1)
        else:
            frase_texto = "Dirección IP incorrecta, vuelve a introducir una dirección IP"
            canvas.create_text(
                ventana3.winfo_screenwidth() // 2,
                ventana3.winfo_screenheight() * 0.7,  # Mover la frase hacia la parte inferior
                text=frase_texto,
                font=("Arial", 18),
                fill="red",
             )
            
    boton_comprobar = tk.Button(
        ventana3, text="Check", command=comprobar_ip
    )
    dar_formato_moderno(boton_comprobar, color_inicial="green", color_resaltado="gray", icono=icono_check)
    boton_comprobar.config(padx=10)
    boton_comprobar.place(relx=0.65, rely=0.5, anchor="center")  # Ubicar el botón en la esquina inferior derecha

    boton_retroceder = tk.Button(
        ventana3, text="Back", command=retroceder_segunda_ventana_desde_tercera
    )
    dar_formato_moderno(boton_retroceder, color_inicial="green", color_resaltado="gray", icono=icono_retroceder)
    boton_retroceder.config(padx=10)
    boton_retroceder.place(relx=0.05, rely=0.95, anchor="sw")  # Colocar en la esquina inferior izquierda
   

    boton_salir = tk.Button(
        ventana3, text="Exit", command=ventana3.destroy
    )
    dar_formato_moderno(boton_salir, color_inicial="red", color_resaltado="gray", icono=icono_salir)
    boton_salir.config(padx=10)
    boton_salir.place(relx=0.95, rely=0.95, anchor="se")  # Ubicar el botón en la esquina inferior derecha


    ventana3.mainloop()


def cuarta_ventana():
    global ventana4, fondo
    ventana4 = tk.Tk()
    ventana4.title("Introducir IP")
    ventana4.attributes('-fullscreen',True)
    icono_check = "check.png"
    icono_retroceder = "icono_retroceder.png"
    icono_salir = "icono_salir.png"

    fondo4 = Image.open(os.path.join(os.getcwd(), "moyseafoodsegundaportada.png"))
    fondo4 = fondo4.resize((ventana4.winfo_screenwidth(), ventana4.winfo_screenheight()), Image.LANCZOS)
    fondo4final = ImageTk.PhotoImage(fondo4)

    canvas = tk.Canvas(ventana4, width=800, height=400)
    canvas.pack(fill="both", expand=True)

    canvas.create_image(0, 0, anchor="nw", image=fondo4final)

    frase_texto = "Introduzca la IP de la etiquetadora a la que deseas volcar la Base de Datos"
    canvas.create_text(
        ventana4.winfo_screenwidth() // 2,
        ventana4.winfo_screenheight() * 0.3,  # Mover la frase hacia la parte inferior
        text=frase_texto,
        font=("Arial", 18),
        fill="white",
    )


    entrada_texto = tk.Entry(ventana4, font = ("Arial", 16), width = 20)
    entrada_texto.place(relx=0.5, rely=0.5, anchor="center")

    def comprobar_ip():
        ip1 = entrada_texto.get()
        if  ip1 == "1":
            llamar_volcado(ip1)
        else:
            frase_texto = "Dirección IP incorrecta, vuelve a introducir una dirección IP"
            canvas.create_text(
                ventana4.winfo_screenwidth() // 2,
                ventana4.winfo_screenheight() * 0.7,  # Mover la frase hacia la parte inferior
                text=frase_texto,
                font=("Arial", 18),
                fill="red",
             )
            
    boton_comprobar = tk.Button(
        ventana4, text="Check", command=comprobar_ip
    )
    dar_formato_moderno(boton_comprobar, color_inicial="green", color_resaltado="gray", icono=icono_check)
    boton_comprobar.config(padx=10)
    boton_comprobar.place(relx=0.65, rely=0.5, anchor="center")  # Ubicar el botón en la esquina inferior derecha

    boton_retroceder = tk.Button(
        ventana4, text="Back", command=retroceder_segunda_ventana_desde_cuarta
    )
    dar_formato_moderno(boton_retroceder, color_inicial="green", color_resaltado="gray", icono=icono_retroceder)
    boton_retroceder.config(padx=10)
    boton_retroceder.place(relx=0.05, rely=0.95, anchor="sw")  # Colocar en la esquina inferior izquierda
   

    boton_salir = tk.Button(
        ventana4, text="Exit", command=ventana4.destroy
    )
    dar_formato_moderno(boton_salir, color_inicial="red", color_resaltado="gray", icono=icono_salir)
    boton_salir.config(padx=10)
    boton_salir.place(relx=0.95, rely=0.95, anchor="se")  # Ubicar el botón en la esquina inferior derecha


    ventana4.mainloop()





def sexta_ventana(opcion):
    global ventana6
    ventana6 = tk.Tk()
    ventana6.title("Resultado")
    ventana6.attributes('-fullscreen',True)
    icono_retroceder = "icono_retroceder.png"
    icono_salir = "icono_salir.png"

    fondo6 = Image.open(os.path.join(os.getcwd(), "moyseafoodsegundaportada.png"))
    fondo6 = fondo6.resize((ventana6.winfo_screenwidth(), ventana6.winfo_screenheight()), Image.LANCZOS)
    fondo6final = ImageTk.PhotoImage(fondo6)

    canvas = tk.Canvas(ventana6, width=800, height=400)
    canvas.pack(fill="both", expand=True)

    canvas.create_image(0, 0, anchor="nw", image=fondo6final)

    if opcion == 1:
        frase_texto = "¡Copia de la Base de Datos Exitosa!"
        canvas.create_text(
            ventana6.winfo_screenwidth() // 2,
            ventana6.winfo_screenheight() * 0.5,  # Mover la frase hacia la parte inferior
            text=frase_texto,
            font=("Arial", 25),
            fill="white",
        )
    elif opcion == 2:
        frase_texto = "¡Exportación de copia exitosa!"
        canvas.create_text(
            ventana6.winfo_screenwidth() // 2,
            ventana6.winfo_screenheight() * 0.5,  # Mover la frase hacia la parte inferior
            text=frase_texto,
            font=("Arial", 25),
            fill="white",
        )
    elif opcion == 3:
        frase_texto = "¡Copia de seguridad exitosa!"
        canvas.create_text(
            ventana6.winfo_screenwidth() // 2,
            ventana6.winfo_screenheight() * 0.5,  # Mover la frase hacia la parte inferior
            text=frase_texto,
            font=("Arial", 25),
            fill="white",
        )
    
    boton_inicio = tk.Button(
        ventana6, text="Inicio", command=retroceder_inicio_desde_sexta
    )
    dar_formato_moderno(boton_inicio, color_inicial="green", color_resaltado="gray", icono=icono_retroceder)
    boton_inicio.config(padx=10)
    boton_inicio.place(relx=0.05, rely=0.95, anchor="sw")  # Colocar en la esquina inferior izquierda
   

    boton_salir = tk.Button(
        ventana6, text="Exit", command=ventana6.destroy
    )
    dar_formato_moderno(boton_salir, color_inicial="red", color_resaltado="gray", icono=icono_salir)
    boton_salir.config(padx=10)
    boton_salir.place(relx=0.95, rely=0.95, anchor="se")

    ventana6.mainloop()


def septima_ventana(opcion):
    global ventana7
    ventana7 = tk.Tk()
    ventana7.title("Error")
    ventana7.attributes('-fullscreen',True)
    icono_retroceder = "icono_retroceder.png"
    icono_salir = "icono_salir.png"

    fondo7 = Image.open(os.path.join(os.getcwd(), "moyseafoodsegundaportada.png"))
    fondo7 = fondo7.resize((ventana7.winfo_screenwidth(), ventana7.winfo_screenheight()), Image.LANCZOS)
    fondo7final = ImageTk.PhotoImage(fondo7)

    canvas = tk.Canvas(ventana7, width=800, height=400)
    canvas.pack(fill="both", expand=True)

    canvas.create_image(0, 0, anchor="nw", image=fondo7final)

    if opcion == 1:
        frase_texto = "No se ha podido realizar la copia de la base de datos"
        canvas.create_text(
            ventana7.winfo_screenwidth() // 2,
            ventana7.winfo_screenheight() * 0.5,  # Mover la frase hacia la parte inferior
            text=frase_texto,
            font=("Arial", 25),
            fill="red",
        )
    elif opcion == 2:
        frase_texto = "No se ha podido realizar el volcado a la etiquetadora"
        canvas.create_text(
            ventana7.winfo_screenwidth() // 2,
            ventana7.winfo_screenheight() * 0.5,  # Mover la frase hacia la parte inferior
            text=frase_texto,
            font=("Arial", 25),
            fill="red",
        )
    elif opcion == 3:
        frase_texto = "No se ha podido realizar la copia de seguridad"
        canvas.create_text(
            ventana7.winfo_screenwidth() // 2,
            ventana7.winfo_screenheight() * 0.5,  # Mover la frase hacia la parte inferior
            text=frase_texto,
            font=("Arial", 25),
            fill="red",
        )
    elif opcion == 4:
        frase_texto = "No se encuentra copia de la BD para su ruta de red"
        canvas.create_text(
            ventana7.winfo_screenwidth() // 2,
            ventana7.winfo_screenheight() * 0.5,  # Mover la frase hacia la parte inferior
            text=frase_texto,
            font=("Arial", 25),
            fill="red",
        )
    elif opcion == 5:
        frase_texto = "No se pudo realizar la copia"
        canvas.create_text(
            ventana7.winfo_screenwidth() // 2,
            ventana7.winfo_screenheight() * 0.5,  # Mover la frase hacia la parte inferior
            text=frase_texto,
            font=("Arial", 25),
            fill="red",
        )
    elif opcion == 6:
        frase_texto = "Error de conexión"
        canvas.create_text(
            ventana7.winfo_screenwidth() // 2,
            ventana7.winfo_screenheight() * 0.5,  # Mover la frase hacia la parte inferior
            text=frase_texto,
            font=("Arial", 25),
            fill="red",
        )

    boton_inicio = tk.Button(
        ventana7, text="Inicio", command=retroceder_inicio_desde_septima
    )
    dar_formato_moderno(boton_inicio, color_inicial="green", color_resaltado="gray", icono=icono_retroceder)
    boton_inicio.config(padx=10)
    boton_inicio.place(relx=0.05, rely=0.95, anchor="sw")  # Colocar en la esquina inferior izquierda
   

    boton_salir = tk.Button(
        ventana7, text="Exit", command=ventana7.destroy
    )
    dar_formato_moderno(boton_salir, color_inicial="red", color_resaltado="gray", icono=icono_salir)
    boton_salir.config(padx=10)
    boton_salir.place(relx=0.95, rely=0.95, anchor="se")

    ventana7.mainloop()


primera_ventana()
