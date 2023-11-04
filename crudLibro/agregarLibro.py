import tkinter as tk
import sqlite3
from entidades.libro import Libro

def crearLibroBD(entradaTitulo, entradaPrecioRep):
    
    titulo = entradaTitulo.get()
    precioReposicion = entradaPrecioRep.get()
    
    nuevoLibro = Libro(titulo, precioReposicion)
    
    conn = sqlite3.connect("./biblioteca.db")
    cursor = conn.cursor()
    
    cursor.execute('''INSERT INTO libros (titulo, precioReposicion, estado) VALUES (?, ?, ?)''', (nuevoLibro._titulo, nuevoLibro._precioReposicion, "Disponible"))
    conn.commit()
    conn.close()

def crearLibro():
    
    ventanaCrearLibro = tk.Tk()
    ventanaCrearLibro.title("Agregar nuevo libro.")
    
    labelTitulo = tk.Label(ventanaCrearLibro, text="Titulo del libro: ")
    labelTitulo.pack()
    
    entradaTitulo = tk.Entry(ventanaCrearLibro)
    entradaTitulo.pack()
    
    labelPrecioRep = tk.Label(ventanaCrearLibro, text="Precio reposicion: ")
    labelPrecioRep.pack()
    
    entradaPrecioRep = tk.Entry(ventanaCrearLibro)
    entradaPrecioRep.pack()
    
    botonAgregarLibro = tk.Button(ventanaCrearLibro, text="Agregar libro", command=crearLibroBD(entradaTitulo, entradaPrecioRep))
    botonAgregarLibro.pack()
    
    ventanaCrearLibro.mainloop()
    
crearLibro()