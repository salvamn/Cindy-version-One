from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from pygame import mixer
from getpass import getuser
from subprocess import Popen
import speech_recognition as sr
import pyttsx3
import threading
import random


# ------------------------------------------------------------------------------------------------------------------------
procesos = []
def texto_a_voz(texto):
    """
    Esta funcion nos permite pasar un texto(string) a voz
    :param texto:
    :return:
    """
    engine = pyttsx3.init()
    engine.setProperty("rate", 130)
    voces = engine.getProperty("voices")
    engine.setProperty("voice", voces[0].id)

    engine.say(texto)
    engine.runAndWait()



def reconocimiento_de_voz():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        audio = r.listen(source)

        try:
            texto = r.recognize_google(audio, language="es-ES")
            print(texto)

            return texto
        except:
            pass


def reproductor():
    if reproductor.opened:
        messagebox.showerror("Error", "No puede abrir mas reproductores")
    reproductor.opened = True

    ventana_reproductor = Tk()
    ventana_reproductor.title("Salva Music Studios")
    ventana_reproductor.resizable(False, False)
    ventana_reproductor.geometry("650x450")
    ventana_reproductor.config(background="#2B2B2B")

    def listbox():
        global lista_musica
        cuadro_para_listbox = Frame(ventana_reproductor, bg="#2B2B2B", width=450, height=300)

        barra = Scrollbar(cuadro_para_listbox, orient=VERTICAL)

        lista_musica = Listbox(cuadro_para_listbox, yscrollcommand=barra.set)
        lista_musica.config(width=70, height=20)

        # configurar scrollbar
        barra.config(command=lista_musica.yview)

        cuadro_para_listbox.place(x=10, y=100)
        barra.pack(side=RIGHT, fill=Y)
        lista_musica.pack()

    def listar_filtrar_carpeta_musica():
        from getpass import getuser
        import os

        """
        Esta funcion me permite añadir todas las cancion con extension .mp3 a una lista.
        Primer paso obtener el nombre de usuario del pc
        Segundo paso pasar el nombre de usuario al directorio
        Tercer paso elegir la extension que deseemos
        Cuarto paso agregar las canciones a una lista
        Quinto paso retornar la lista.
        """

        nombre_usuario = getuser()
        directorio = rf"C:\Users\{nombre_usuario}\Music"
        extension = ".mp3"

        canciones = [cancion for cancion in os.listdir(directorio) if cancion.lower().endswith(extension)]

        return canciones


    def escoger_cancion_dos(cancion):
        try:
            nombre_usuario = getuser()
            directorio = rf"C:\Users\{nombre_usuario}\Music\{cancion}"
            mixer.init()
            mixer.music.load(directorio)
            mixer.music.set_volume(0.7)
            mixer.music.play()
        except Exception as e:
            print(e)

    def pausar():
        print("Se pauso la cancion")
        mixer.music.pause()

    def despausar():
        print("Se quito la pausa")
        mixer.music.unpause()

    def seleccionando_item():
        seleccion = lista_musica.get(ANCHOR)
        escoger_cancion_dos(seleccion)

    escoger_cancion_dos(listar_filtrar_carpeta_musica()[1])

    Label(ventana_reproductor, text="SalvaMusicStudios", font=("Dubai", 20, "bold"), background="#2B2B2B",
          foreground="White").place(
        x=200, y=10)

    listbox()

    contador = 0
    for i in listar_filtrar_carpeta_musica():
        lista_musica.insert(contador, i)
        contador += 1

    boton_play = Button(ventana_reproductor, text="Reproducir", width=20, height=2, bg="White",
                        command=seleccionando_item)
    boton_play.place(x=475, y=120)
    boton_pausa = Button(ventana_reproductor, text="Pausa", width=20, height=2, bg="White", command=pausar)
    boton_pausa.place(x=475, y=180)
    boton_despausar = Button(ventana_reproductor, text="Sacar Pausa", width=20, height=2, bg="White", command=despausar)
    boton_despausar.place(x=475, y=240)
    Label(ventana_reproductor, text="Salvador Mellado ©", bg="#2B2B2B", fg="White", font=("Dubai", 10, "bold")).place(
        x=500, y=400)

    ventana_reproductor.wait_window()
    reproductor.opened = False


# -----------------------------------------------------------------------------------------------------------------------

"""
Esta seccion nos permite configurar funciones basicas de la ventana como las siguientes:
1 - Desactivamos el redimenzionamiento de la ventana
2 - Damos un ancho y alto a la ventana
3 - Damos un titulo
4 - asignamos un icono
5 - asignamos un color de fondo a la ventana
"""
ventana = Tk()
ventana.resizable(False, False)
ventana.geometry("420x400")
ventana.title("Ey Cindy")
ventana.iconbitmap("img/icons8_businesswoman.ico")
ventana.config(bg="#2B2B2B")

# -----------------------------------------------------------------------------------------------------------------------
"""
En esta seccion creamos un frame y un listbox con barra de desplazamiento
1 - Primero se crea el frame
    - se le pasa la ventana master como primer parametro
    - como segundo parametro le pasamos el color de fondo
    - tercer y cuarto parametro le damos tamaño al frame
2 - Creamos la barra de dezplazamiento
    - le pasamos el master en este caso el frame
    - y como ultimo parametro le damo la orientacion
3 - En la tercera parte se crea el listbox
    - le pasamos el frame
    - le pasamos la barra y la seteamos
4 - le damos dimension al listbox
5 - insertamos los strings
"""

cuadro_listbox = Frame(ventana, bg="Red", width=450, height=300)

barra = Scrollbar(cuadro_listbox, orient=VERTICAL)

lista = Listbox(cuadro_listbox, yscrollcommand=barra.set)
lista.config(width=40, height=20)

# configurar scrollbar
barra.config(command=lista.yview)

cuadro_listbox.place(x=10, y=60)
barra.pack(side=RIGHT, fill=Y)
lista.pack()

lista.insert(0, "Reproducir Musica")
lista.insert(1, "Bloc de Notas")
lista.insert(3, "Pycharm")
lista.insert(4, "Visual Studio Code")
lista.insert(5, "Intellij Idea")


# ------------------------------------------------------------------------------------------------------------------------

def seleccion_de_item():
    select = lista.get(lista.curselection())
    print(select)

    if select == "Reproducir Musica":
        reproductor()
        try:
            mixer.music.stop()
        except Exception as e:
            print(e)
        print(select)
    elif select == "Bloc de Notas":
        Popen("Notepad.exe")







def seleccion_por_voz():
    texto = reconocimiento_de_voz()

    if texto == "Música Pendeja" or texto == "música pendeja" or texto == "musica pendeja" or texto == "música p******" or texto == "música":
        Popen(reproductor())
        try:
            mixer.music.stop()
        except Exception as e:
            print(e)
    elif texto == "Bloc" or texto == "bloc" or texto == "Notas" or texto == "notas":
        Popen("Notepad.exe")
    elif texto == "Navegador" or texto == "navegador":
        Popen("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")



def worker_seleccion():
    p = threading.Thread(target=seleccion_por_voz)
    procesos.append(p)
    p.start()
    p.is_alive()



reproductor.opened = False
# ------------------------------------------------------------------------------------------------------------------------

Label(ventana, text="Cindy Asistente Virtual", bg="#2B2B2B", fg="White", font="Dubai 18 bold").place(x=17, y=10)

Button(ventana, text="Necesito esto", width=14, height=2, command=seleccion_de_item).place(x=300, y=80)

# Imagen cindy
img = Image.open("img/cindy.png")
img = img.resize((100, 200), Image.ANTIALIAS)  # redimensionamos la imagen Ancho x Alto
img = ImageTk.PhotoImage(img)




Button(ventana, text="Hablar", image=img, command=worker_seleccion).place(x=300, y=150)
Label(ventana, text="Habla con Cindy", font=("Dubai", 13), bg="#2B2B2B", fg="White").place(x=295, y=355)

# ------------------------------------------------------------------------------------------------------------------------


ventana.mainloop()
