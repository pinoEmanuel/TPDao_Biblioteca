import tkinter as tk
import sqlite3

def consultarLibrosBD(entradaTitulo):
    
    libro = entradaTitulo.get()
    
    conn = sqlite3.connect("./biblioteca.db")
    cursor = conn.cursor()
    sql = '''SELECT l.* From libros l WHERE l.titulo = ?'''
    cursor.execute(sql, (libro))
    
    resultado = cursor.fetchall()
    
    for libro in resultado:
        grilla.insert(tk.END, libro)
        
    conn.commit()
    conn.close()

def consultarLibros():
    
    ventanaConsultarLibros = tk.Tk()
    ventanaConsultarLibros.title("Consultar libros")
    
    labelLibro = tk.Label(ventanaConsultarLibros, text="Titulo del libro: ")
    labelLibro.pack()
    
    entradaTitulo = tk.Entry(ventanaConsultarLibros)
    entradaTitulo.pack()
    
    botonConsultar = tk.Button(ventanaConsultarLibros, text="Consultar", command=consultarLibrosBD(entradaTitulo))
    botonConsultar.pack()
    
    grilla = tk.Listbox(ventanaConsultarLibros)
    grilla.pack()
    
    ventanaConsultarLibros.mainloop()

consultarLibros()
