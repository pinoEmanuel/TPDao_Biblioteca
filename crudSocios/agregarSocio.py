import tkinter as tk
import sqlite3
from entidades.socio import Socio

def crearSocioBD(entradaNombre, entradaApellido):
    
    nombre = entradaNombre.get()
    apellido = entradaApellido.get()
    
    nuevoSocio = Socio(nombre, apellido)
    
    conn = sqlite3.connect("./biblioteca.db")
    cursor = conn.cursor()
    
    cursor.execute('''INSERT INTO socios (nombre, apellido) VALUES (?, ?)''', (nuevoSocio._nombre, nuevoSocio._apellido))
    conn.commit()
    conn.close()

def crearSocio():
    
    ventanaCrearSocio = tk.Tk()
    ventanaCrearSocio.title("Agregar nuevo socio.")
    
    labelNombre = tk.Label(ventanaCrearSocio, text="Nombre de socio: ")
    labelNombre.pack()
    
    entradaNombre = tk.Entry(ventanaCrearSocio)
    entradaNombre.pack()
    
    labelApellido = tk.Label(ventanaCrearSocio, text="Apellido: ")
    labelApellido.pack()
    
    entradaApellido = tk.Entry(ventanaCrearSocio)
    entradaApellido.pack()
    
    botonAgregarSocio = tk.Button(ventanaCrearSocio, text="Agregar socio", command=crearSocioBD(entradaNombre, entradaApellido))
    botonAgregarSocio.pack()
    
    ventanaCrearSocio.mainloop()
    
crearSocio()